"""Shared scoring and database utilities for rotor configuration workers."""
import hashlib
import os
import sqlite3
from typing import Callable, Dict, List, Optional, Tuple

N = 64


def get_db_path() -> str:  # pragma: no cover
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.normpath(os.path.join(here, '..', 'rotor_configurations.db'))


def get_connection() -> sqlite3.Connection:  # pragma: no cover
    """Open a database connection in autocommit mode for explicit transaction control.

    WAL journal mode is enforced on every connection so that DB Browser (or any
    other read-only tool) can query the database concurrently while workers are
    writing without either side being blocked.
    """
    conn = sqlite3.connect(get_db_path(), timeout=30, check_same_thread=False)
    conn.isolation_level = None
    conn.execute('PRAGMA journal_mode=WAL')
    conn.execute('PRAGMA synchronous=NORMAL')
    return conn


def ring_dist(a: int, b: int) -> int:
    """Circular distance on a ring of N positions (0 and N-1 are adjacent)."""
    d = abs(a - b)
    return min(d, N - d)


def compute_score(perm: List[int]) -> Dict:
    """Return all five complexity score components plus total for a permutation."""
    dists = [ring_dist(perm[i], i) for i in range(N)]

    # C1: Ring displacement magnitude (30 pts)
    c1 = 30.0 * (sum(dists) / N) / 32.0

    # C2: Fixed point score (20 pts)
    fixed_points = sum(1 for i in range(N) if perm[i] == i)
    c2 = 20.0 * (N - fixed_points) / N

    # C3: Cycle structure (10 pts)
    visited = [False] * N
    cycles = []
    for start in range(N):
        if not visited[start]:
            length, curr = 0, start
            while not visited[curr]:
                visited[curr] = True
                curr = perm[curr]
                length += 1
            cycles.append(length)
    short_cycles = sum(1 for c in cycles if c <= 2)
    mean_cycle_len = sum(cycles) / len(cycles)
    c3 = max(0.0, min(10.0,
        5.0 * (1.0 - short_cycles / 32.0) + 5.0 * mean_cycle_len / 32.0
    ))

    # C4: Consecutive run penalty (20 pts)
    max_run = asc = desc = 1
    for i in range(1, N):
        asc  = asc  + 1 if perm[i] == perm[i - 1] + 1 else 1
        desc = desc + 1 if perm[i] == perm[i - 1] - 1 else 1
        max_run = max(max_run, asc, desc)
    c4 = 20.0 * max(0.0, 1.0 - (max_run - 1) / 8.0)

    # C5: Ring displacement uniformity -- 10th percentile (20 pts)
    p10 = sorted(dists)[int(0.1 * N)]
    c5 = 20.0 * p10 / 32.0

    total = min(100.0, max(0.0, c1 + c2 + c3 + c4 + c5))
    return {
        'score_total':           round(total, 4),
        'score_c1_displacement': round(c1,    4),
        'score_c2_fixed_points': round(c2,    4),
        'fixed_point_count':     fixed_points,
        'score_c3_cycles':       round(c3,    4),
        'score_c4_runs':         round(c4,    4),
        'score_c5_uniformity':   round(c5,    4),
    }


def make_rotation_key(perm: List[int]) -> str:
    """16-char hex key identical for all rotations and the element-wise reverse."""
    rev = perm[::-1]
    best = None
    for k in range(N):
        for src in (perm, rev):
            rot = tuple(src[(i + k) % N] for i in range(N))
            if best is None or rot < best:
                best = rot
    return hashlib.sha256(str(best).encode()).hexdigest()[:16]


def claim_permutation(conn: sqlite3.Connection, perm: List[int], key: str) -> Optional[int]:
    """Atomically claim a database slot before scoring.

    Uses BEGIN IMMEDIATE to acquire a write lock, checks for a duplicate rotation_key,
    and if unique, inserts a placeholder row with NULL scores. Returns the new row id
    on success, or None if the key already exists or a lock timeout occurs. Score values
    are written separately by update_scores() once scoring is complete.
    """
    p_cols = ', '.join(f'p{i}' for i in range(N))
    sql = (
        f'INSERT INTO rotor_configurations '
        f'({p_cols}, rotation_key) VALUES ({", ".join(["?"] * (N + 1))})'
    )
    try:
        conn.execute('BEGIN IMMEDIATE')
        if conn.execute(
            'SELECT 1 FROM rotor_configurations WHERE rotation_key = ?', (key,)
        ).fetchone():
            conn.execute('ROLLBACK')
            return None
        cursor = conn.execute(sql, list(perm) + [key])
        conn.execute('COMMIT')
        return cursor.lastrowid
    except Exception:  # pragma: no cover - requires forcing a mid-transaction DB error, not reachable via normal test injection
        try:
            conn.execute('ROLLBACK')
        except Exception:
            pass
        return None


def update_scores(conn: sqlite3.Connection, row_id: int, scores: Dict) -> None:
    """Update a claimed placeholder row with its computed score values."""
    conn.execute(
        'UPDATE rotor_configurations SET '
        'score_total = ?, score_c1_displacement = ?, score_c2_fixed_points = ?, '
        'fixed_point_count = ?, score_c3_cycles = ?, score_c4_runs = ?, '
        'score_c5_uniformity = ? WHERE id = ?',
        [
            scores['score_total'], scores['score_c1_displacement'],
            scores['score_c2_fixed_points'], scores['fixed_point_count'],
            scores['score_c3_cycles'], scores['score_c4_runs'],
            scores['score_c5_uniformity'], row_id,
        ]
    )


def run_seeded_batch(
    generate_fn: Callable[[int], List[int]],
    seed_start: int,
    seed_count: int,
    conn: Optional[sqlite3.Connection] = None,
) -> Tuple[int, int, int]:
    """Process exactly seed_count seeds; insert and score any new permutations.

    Unlike run_batch() in individual worker scripts (which loops until a target
    insertion count is reached), this function processes a fixed window of seeds
    regardless of how many are duplicates. This makes it suitable for the
    orchestrator, which needs a predictable amount of work per round and must
    be able to detect when a seed region is exhausted (all duplicates).

    Pass conn to inject a connection (tests / orchestrator reuse). When conn is
    None a fresh production connection is opened and closed automatically.

    Returns (inserted, skipped, next_seed).
    """
    own_conn = conn is None
    if own_conn:
        conn = get_connection()  # pragma: no cover
    inserted = skipped = 0
    seed = seed_start
    for _ in range(seed_count):
        perm = generate_fn(seed)
        key = make_rotation_key(perm)
        row_id = claim_permutation(conn, perm, key)
        if row_id is not None:
            update_scores(conn, row_id, compute_score(perm))
            inserted += 1
        else:
            skipped += 1
        seed += 1
    if own_conn:
        conn.close()  # pragma: no cover
    return inserted, skipped, seed
