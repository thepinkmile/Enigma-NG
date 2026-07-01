# Rotor Configuration Generation Process

**Last Updated:** 2026-07-02

---

## 1. Overview

This document describes the process used to generate and select the pre-configured rotor wiring
maps stored in `rotor_configurations.db`. These maps define how each of the 64 input positions
on a rotor is wired to an output position, equivalent to the scrambler wiring inside the rotors
of the original Enigma cipher machines, extended here to a base-64 character set.

Each wiring map is a permutation of the integers 0-63, where each integer represents one of the
64 characters on the rotor face. The rotor face is treated as a cylinder (ring buffer): position
0 and position 63 are physically adjacent, which affects distance calculations throughout the
scoring algorithm.

The goal is to produce a curated set of **1,000 cryptographically meaningful wiring maps**
distributed evenly across a 0-100 complexity scale, with roughly 100 maps per 10-point band.

---

## 2. Datastore

**File:** `src/Data/configurations/rotor_configurations.db`
**Format:** SQLite 3

### 2.1 Schema

```sql
CREATE TABLE rotor_configurations (
    id                   INTEGER PRIMARY KEY AUTOINCREMENT,
    reflected_index      INTEGER  DEFAULT NULL,
    notes                TEXT     DEFAULT NULL,
    -- Permutation: p0 is the output for input position 0, p63 for input position 63
    p0  INTEGER, p1  INTEGER, p2  INTEGER, p3  INTEGER, p4  INTEGER, p5  INTEGER,
    p6  INTEGER, p7  INTEGER, p8  INTEGER, p9  INTEGER, p10 INTEGER, p11 INTEGER,
    p12 INTEGER, p13 INTEGER, p14 INTEGER, p15 INTEGER, p16 INTEGER, p17 INTEGER,
    p18 INTEGER, p19 INTEGER, p20 INTEGER, p21 INTEGER, p22 INTEGER, p23 INTEGER,
    p24 INTEGER, p25 INTEGER, p26 INTEGER, p27 INTEGER, p28 INTEGER, p29 INTEGER,
    p30 INTEGER, p31 INTEGER, p32 INTEGER, p33 INTEGER, p34 INTEGER, p35 INTEGER,
    p36 INTEGER, p37 INTEGER, p38 INTEGER, p39 INTEGER, p40 INTEGER, p41 INTEGER,
    p42 INTEGER, p43 INTEGER, p44 INTEGER, p45 INTEGER, p46 INTEGER, p47 INTEGER,
    p48 INTEGER, p49 INTEGER, p50 INTEGER, p51 INTEGER, p52 INTEGER, p53 INTEGER,
    p54 INTEGER, p55 INTEGER, p56 INTEGER, p57 INTEGER, p58 INTEGER, p59 INTEGER,
    p60 INTEGER, p61 INTEGER, p62 INTEGER, p63 INTEGER,
    -- Scoring
    score_total          REAL     DEFAULT NULL,
    score_c1_displacement REAL    DEFAULT NULL,
    score_c2_fixed_points REAL    DEFAULT NULL,
    fixed_point_count    INTEGER  DEFAULT NULL,
    score_c3_cycles      REAL     DEFAULT NULL,
    score_c4_runs        REAL     DEFAULT NULL,
    score_c5_uniformity  REAL     DEFAULT NULL,
    -- Deduplication
    rotation_key         TEXT     DEFAULT NULL,
    -- Selection
    selected             INTEGER  DEFAULT 0   -- 0 = False, 1 = True
);

CREATE INDEX idx_rotation_key ON rotor_configurations (rotation_key);
```

### 2.2 Column Reference

| Column | Description |
| --- | --- |
| `id` | Auto-incremented primary key |
| `reflected_index` | ID of the paired/reflected configuration (populated separately) |
| `notes` | Free-text notes for manual annotation |
| `p0`-`p63` | The permutation: `pN` is the output wiring for input position N |
| `score_total` | Overall complexity score (0-100) |
| `score_c1_displacement` | Component 1 sub-score (ring displacement magnitude) |
| `score_c2_fixed_points` | Component 2 sub-score (fixed point penalty) |
| `fixed_point_count` | Raw count of positions where pN = N |
| `score_c3_cycles` | Component 3 sub-score (cycle structure) |
| `score_c4_runs` | Component 4 sub-score (consecutive run penalty) |
| `score_c5_uniformity` | Component 5 sub-score (displacement uniformity) |
| `rotation_key` | 16-char canonical dedup key covering all rotations and the reverse |
| `selected` | 1 if this row is in the final 1,000; 0 otherwise |

---

## 3. Row 1: Passthrough Map

ID 1 is always reserved for the identity permutation (pN = N for all N). This is the passthrough
map used for testing and as a known-baseline reference. Its complexity score is 0 by design and
it is always marked `selected = 1`.

---

## 4. Generation Process

### 4.1 Candidate Pool

A large candidate pool is generated before selection, targeting an even
distribution across all 10 score bands. The pool is built by parallel background
workers, each targeting a specific region of the complexity space:

| Worker | Strategy | Target Band | Seed Namespace |
| --- | --- | --- | --- |
| A | Near-identity (3-15 random swaps from identity) | ~0-25 | 0+ |
| B | Near-shift-32 (8-24 swaps from shift-by-32 base) | ~55-90 | 1,000,000+ |
| C | Pure random Fisher-Yates | Broad middle | 2,000,000+ |
| D | Displacement-maximising (far-half selection) | ~60-95 | 3,000,000+ |
| E | Stride-swap base (block pair swaps, d in {1,2,4,8}) + 0-6 swaps | 30-49 | 4,000,000+ |
| F | Partial Fisher-Yates (30 of 64 positions shuffled) | 20-29 | 8,000,000+ |
| G | Shift-by-32 base with 30-32 adjacent pair swaps | 80-89 (small design space) | 9,000,000+ |
| H | Top-quarter displacement-maximising (aggressive far selection) | 80-89 (large design space) | 10,000,000+ |

Multiple slots of the same worker type (E2/E3, F2/F3, G2/G3) can run
concurrently from independent seed namespaces. All slots are registered in the
orchestrator and selectable via the `--workers` flag (see Section 7.6).

Each worker generates permutations in **batches of 1,000 seeds**, writing results
to the database after each batch. This allows the process to be paused, inspected,
or redirected between batches without losing progress.

### 4.2 Duplicate Filtering

Before a candidate is written to the database, it is tested against all existing rows and
rejected if any of the following conditions are true:

1. **Rotational duplicate:** The candidate is a cyclic left or right shift of an existing row
   (i.e., `P[i] = Q[(i + k) mod 64]` for any shift `k` and existing permutation `Q`).

2. **Reverse duplicate:** The candidate is the exact element-wise reverse of an existing row
   (i.e., `P[i] = Q[63 - i]` for all `i` and existing permutation `Q`).

The passthrough identity row (ID 1) is exempt from both checks.

### 4.3 Final Selection

Once the candidate pool is complete, the final 1,000 rows are selected as follows:

1. Divide the 0-100 complexity range into 10 bands: 0-9, 10-19, 20-29, ..., 90-100.
2. From each band, select approximately 100 rows.
3. Within each band, prefer rows with higher `score_c4_runs` and `score_c5_uniformity`
   (better structural quality), using `score_c2_fixed_points` and `fixed_point_count` as
   tiebreakers to ensure a mix of derangements and maps with fixed points.
4. Mark selected rows with `selected = 1`.

The individual component scores stored for every candidate row make it possible to re-run
this selection step with different criteria without regenerating the full pool.

---

## 5. Complexity Scoring Algorithm

All scores are in the range 0-100. The total score is the sum of the five components below.

### Component 1 -- Ring Displacement Magnitude (30 points)

Measures how far each character travels from its input position on average. Distance is
calculated as a ring/cylinder distance so that positions 0 and 63 are treated as adjacent.

```text
ring_dist(i) = min(|P[i] - i|, 64 - |P[i] - i|)
score_c1 = 30 * mean(ring_dist) / 32
```

Maximum mean ring distance = 32 (achieved when every element maps to position i+32 mod 64).

### Component 2 -- Fixed Point Score (20 points)

Measures how many positions map to themselves. Stored both as a component of the total score
and as the dedicated `score_c2_fixed_points` and `fixed_point_count` columns so that maps with
fixed points can be deliberately selected when required (unlike the original Enigma machine,
which enforced no fixed points, this system allows them).

```text
fixed_points = count of i where P[i] = i
score_c2 = 20 * (64 - fixed_points) / 64
```

### Component 3 -- Cycle Structure (10 points)

Decomposes the permutation into disjoint cycles. Long, interlocking cycles are harder to
cryptanalyse than short transpositions or fixed points.

```text
short_cycles = count of cycles with length 1 or 2
score_c3 = (5 * (1 - short_cycles / 32)) + (5 * mean_cycle_length / 32)
```

### Component 4 -- Consecutive Run Penalty (20 points)

Finds the longest ascending or descending run of consecutive values anywhere in the permutation.
Long runs reveal structure and reduce scrambling effectiveness.

```text
max_run = length of longest ascending or descending consecutive run
score_c4 = 20 * max(0, 1 - (max_run - 1) / 8)
```

A permutation with no run longer than 1 scores the full 20 points. A run of 9 or more scores 0.

### Component 5 -- Ring Displacement Uniformity (20 points)

Uses the 10th percentile of ring distances to ensure that even the most weakly-scrambled
positions contribute meaningfully. Prevents a permutation from scoring well on Component 1
through a few very large displacements while leaving many positions near-static.

```text
score_c5 = 20 * percentile_10(ring_dist) / 32
```

Uses the same ring distance values calculated in Component 1.

### Score Summary

| Component | Metric | Max Points |
| --- | --- | --- |
| C1 | Ring displacement magnitude | 30 |
| C2 | Fixed point score | 20 |
| C3 | Cycle structure | 10 |
| C4 | Consecutive run penalty | 20 |
| C5 | Ring displacement uniformity | 20 |
| **Total** | | **100** |

### Reference Benchmarks

| Permutation | C1 | C2 | C3 | C4 | C5 | Total |
| --- | --- | --- | --- | --- | --- | --- |
| Identity `[0, 1, ..., 63]` | 0 | 0 | 0 | 0 | 0 | ~0 |
| Reverse `[63, 62, ..., 0]` | ~3 | 20 | ~6 | 20 | ~1 | ~50 |
| Shift-by-32 `[32, 33, ..., 63, 0, 1, ..., 31]` | 30 | 20 | ~5 | 0 | 30* | ~85* |
| Good random permutation | 20-28 | 16-20 | 6-10 | 14-20 | 8-16 | ~70-90 |

*Shift-by-32 has max ring displacement but a run of 32, so C4 = 0 and C5 is penalised by the run.

---

## 6. Re-running the Process

Re-runs are fully additive. Workers never delete existing rows. Permutations whose
`rotation_key` already exists are automatically discarded, so any worker can be run at
any time without risk of losing or duplicating existing data.

To add more candidates to the pool:

1. Run any worker script using the `next_seed` value reported at the end of the previous
   batch. Existing permutations are skipped automatically.
2. Multiple workers may run concurrently -- each worker atomically claims a database row
   (inserting it with NULL scores) before computing scores. This prevents two workers from
   ever spending time on the same permutation.
3. Once the pool is large enough, re-run the selection query from Section 4.3 to refresh
   the `selected = 1` flags for the new best 1,000 candidates.

To generate a completely fresh pool (rare -- requires a manual DBA action):

1. Keep all rows where `selected = 1` to preserve the curated set.
2. Manually delete rows where `selected = 0` via a direct SQL query.
   This step is never performed by the worker scripts themselves.
3. Re-seed each worker from its default starting seed.

The scoring algorithm is fully defined in Section 5 and can be re-implemented independently
in any language as long as the ring-distance convention (Section 5, Component 1) is respected.

---

## 7. Worker Scripts

All worker scripts live in `src/Data/configurations/workers/`. Run each from that directory:

```powershell
cd src\Data\configurations\workers
python worker_a.py [seed_start] [batch_size]
```

Each script accepts two optional positional arguments:

- `seed_start` -- the first random seed to use (default varies per worker; see table below)
- `batch_size` -- number of permutations to insert per batch (default: 100)

On completion each script prints `next_seed=<value>`. Pass this value as `seed_start` when
triggering the next batch to avoid repeating the same candidates.

| Worker | File | Default seed_start | Strategy | Target band |
| --- | --- | --- | --- | --- |
| A | `worker_a.py` | 0 | Near-identity (3-15 random swaps from identity) | ~0-25 |
| B | `worker_b.py` | 1,000,000 | Near-shift-32 (8-24 swaps from shift-by-32 base) | ~55-90 |
| C | `worker_c.py` | 2,000,000 | Pure random Fisher-Yates | Broad middle |
| D | `worker_d.py` | 3,000,000 | Displacement-maximising (far-half selection) | ~60-95 |
| E | `worker_e.py` | 4,000,000 | Stride-swap base (d in {1,2,4,8}) + 0-6 transpositions | 30-49 |
| F | `worker_f.py` | 8,000,000 | Partial Fisher-Yates (30/64 positions shuffled) | 20-29 |
| G | `worker_g.py` | 9,000,000 | Shift-by-32 + 30-32 adjacent pair swaps | 80-89 |

### 7.1 Shared Utilities (`worker_utils.py`)

```python
"""Shared scoring and database utilities for rotor configuration workers."""
import hashlib
import os
import sqlite3
from typing import Dict, List, Optional

N = 64


def get_db_path() -> str:
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.normpath(os.path.join(here, '..', 'rotor_configurations.db'))


def get_connection() -> sqlite3.Connection:
    """Open a database connection in autocommit mode for explicit transaction control."""
    conn = sqlite3.connect(get_db_path(), timeout=30, check_same_thread=False)
    conn.isolation_level = None
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
    except Exception:
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
```

### 7.2 Worker A -- Low Displacement Bias (`worker_a.py`)

```python
"""Worker A: low-displacement bias.

Starts from the identity permutation and applies a small number of random
transpositions (3 to 15). Targets the low-complexity end of the scoring
distribution (approximate score range: 5-50).

Usage: python worker_a.py [seed_start=0] [batch_size=100]
"""
import random
import sys

from worker_utils import (N, claim_permutation, compute_score, get_connection,
                          make_rotation_key, update_scores)


def generate(seed: int) -> list:
    rng = random.Random(seed)
    perm = list(range(N))
    for _ in range(rng.randint(3, 15)):
        i, j = rng.sample(range(N), 2)
        perm[i], perm[j] = perm[j], perm[i]
    return perm


def run_batch(seed_start: int = 0, batch_size: int = 100) -> int:
    conn = get_connection()
    inserted = skipped = 0
    seed = seed_start
    while inserted < batch_size:
        perm = generate(seed)
        seed += 1
        key = make_rotation_key(perm)
        row_id = claim_permutation(conn, perm, key)
        if row_id is not None:
            scores = compute_score(perm)
            update_scores(conn, row_id, scores)
            inserted += 1
            print(f'[A] {inserted:>3}/{batch_size}  id={row_id:<6}  '
                  f'score={scores["score_total"]:6.2f}  seed={seed - 1}')
        else:
            skipped += 1
    conn.close()
    print(f'[A] Done. inserted={inserted}  skipped={skipped}  next_seed={seed}')
    return seed


if __name__ == '__main__':
    s = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    b = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    run_batch(s, b)
```

### 7.3 Worker B -- High Displacement Bias (`worker_b.py`)

```python
"""Worker B: high-displacement bias.

Starts from the shift-by-32 permutation (p[i] = (i + 32) % 64, the maximum
possible mean ring displacement base) and applies 8 to 24 random transpositions.
Targets the high-complexity end (approximate score range: 55-90).

Usage: python worker_b.py [seed_start=1000000] [batch_size=100]
"""
import random
import sys

from worker_utils import (N, claim_permutation, compute_score, get_connection,
                          make_rotation_key, update_scores)

_BASE = [(i + N // 2) % N for i in range(N)]


def generate(seed: int) -> list:
    rng = random.Random(seed)
    perm = _BASE[:]
    for _ in range(rng.randint(8, 24)):
        i, j = rng.sample(range(N), 2)
        perm[i], perm[j] = perm[j], perm[i]
    return perm


def run_batch(seed_start: int = 1_000_000, batch_size: int = 100) -> int:
    conn = get_connection()
    inserted = skipped = 0
    seed = seed_start
    while inserted < batch_size:
        perm = generate(seed)
        seed += 1
        key = make_rotation_key(perm)
        row_id = claim_permutation(conn, perm, key)
        if row_id is not None:
            scores = compute_score(perm)
            update_scores(conn, row_id, scores)
            inserted += 1
            print(f'[B] {inserted:>3}/{batch_size}  id={row_id:<6}  '
                  f'score={scores["score_total"]:6.2f}  seed={seed - 1}')
        else:
            skipped += 1
    conn.close()
    print(f'[B] Done. inserted={inserted}  skipped={skipped}  next_seed={seed}')
    return seed


if __name__ == '__main__':
    s = int(sys.argv[1]) if len(sys.argv) > 1 else 1_000_000
    b = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    run_batch(s, b)
```

### 7.4 Worker C -- Pure Random (`worker_c.py`)

```python
"""Worker C: pure random Fisher-Yates shuffle.

No bias applied. Seed range starts at 2,000,000 to ensure independence from
Workers A and B. Covers the broad middle of the complexity distribution.

Usage: python worker_c.py [seed_start=2000000] [batch_size=100]
"""
import random
import sys

from worker_utils import (N, claim_permutation, compute_score, get_connection,
                          make_rotation_key, update_scores)


def generate(seed: int) -> list:
    rng = random.Random(seed)
    perm = list(range(N))
    rng.shuffle(perm)
    return perm


def run_batch(seed_start: int = 2_000_000, batch_size: int = 100) -> int:
    conn = get_connection()
    inserted = skipped = 0
    seed = seed_start
    while inserted < batch_size:
        perm = generate(seed)
        seed += 1
        key = make_rotation_key(perm)
        row_id = claim_permutation(conn, perm, key)
        if row_id is not None:
            scores = compute_score(perm)
            update_scores(conn, row_id, scores)
            inserted += 1
            print(f'[C] {inserted:>3}/{batch_size}  id={row_id:<6}  '
                  f'score={scores["score_total"]:6.2f}  seed={seed - 1}')
        else:
            skipped += 1
    conn.close()
    print(f'[C] Done. inserted={inserted}  skipped={skipped}  next_seed={seed}')
    return seed


if __name__ == '__main__':
    s = int(sys.argv[1]) if len(sys.argv) > 1 else 2_000_000
    b = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    run_batch(s, b)
```

### 7.5 Worker D -- Displacement-Maximising (`worker_d.py`)

```python
"""Worker D: displacement-maximising strategy.

For each position i (processed in randomly shuffled order), the output value is
chosen at random from the half of remaining unused values that are furthest from i
on the ring. This biases permutations toward higher ring displacements without
being fully deterministic. Seed range starts at 3,000,000.

Usage: python worker_d.py [seed_start=3000000] [batch_size=100]
"""
import random
import sys

from worker_utils import (N, claim_permutation, compute_score, get_connection,
                          make_rotation_key, ring_dist, update_scores)


def generate(seed: int) -> list:
    rng = random.Random(seed)
    perm = [None] * N
    positions = list(range(N))
    rng.shuffle(positions)
    available = list(range(N))
    for i in positions:
        available.sort(key=lambda v: ring_dist(v, i), reverse=True)
        top_half = available[:max(1, len(available) // 2)]
        chosen = rng.choice(top_half)
        perm[i] = chosen
        available.remove(chosen)
    return perm


def run_batch(seed_start: int = 3_000_000, batch_size: int = 100) -> int:
    conn = get_connection()
    inserted = skipped = 0
    seed = seed_start
    while inserted < batch_size:
        perm = generate(seed)
        seed += 1
        key = make_rotation_key(perm)
        row_id = claim_permutation(conn, perm, key)
        if row_id is not None:
            scores = compute_score(perm)
            update_scores(conn, row_id, scores)
            inserted += 1
            print(f'[D] {inserted:>3}/{batch_size}  id={row_id:<6}  '
                  f'score={scores["score_total"]:6.2f}  seed={seed - 1}')
        else:
            skipped += 1
    conn.close()
    print(f'[D] Done. inserted={inserted}  skipped={skipped}  next_seed={seed}')
    return seed


if __name__ == '__main__':
    s = int(sys.argv[1]) if len(sys.argv) > 1 else 3_000_000
    b = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    run_batch(s, b)
```

### 7.5 Worker E -- Mid-Range Band 30-49 (`worker_e.py`)

Generates permutations using a stride-swap base: positions are swapped in pairs
at stride distance `d` (chosen randomly from {1, 2, 4, 8}), followed by 0-6
random transpositions. This reliably produces scores in the 30-49 band (100% hit
rate), filling the gap left by Workers A-D whose strategies naturally avoid this
region. Seed namespace: 4,000,000+. Slots E2/E3/E4 use seed namespaces 5M/6M/7M.

### 7.6 Worker F -- Low-Mid Band 20-29 (`worker_f.py`)

Generates permutations by applying a partial Fisher-Yates shuffle to exactly 30
of the 64 positions (chosen at random), leaving the remaining 34 positions fixed.
The mix of moderate displacement and many fixed points places ~80% of output in
the 20-29 score band, with the remaining ~20% in the adjacent 10-19 band.
Seed namespace: 8,000,000+. Slots F2/F3 use seed namespaces 8,500,000/8,750,000.

### 7.7 Worker G -- High Band 80-89 (`worker_g.py`)

Generates permutations using a shift-by-32 base (maximum ring displacement) with
30-32 of the 32 non-overlapping adjacent pairs (positions 0-1, 2-3, ..., 62-63)
randomly selected and swapped. This achieves 100% hit rate in the 80-89 band
because:

- **C1** stays near 29 (ring distance drops from 32 to 31 per swapped pair)
- **C2** = 20 (shift-by-32 base guarantees no fixed points)
- **C4** = 17.5 (adjacent pair swaps cap max_run at 2, breaking all ascending runs)
- **C5** stays near 19.4 (all ring distances are 31)

**Note:** Worker G has a small design space (~529 distinct pair selections). After
rotational deduplication it is exhausted within a few hundred batches and is not
suitable for large-scale 80-89 filling. Use Worker H for high-volume 80-89 generation.

Seed namespace: 9,000,000+. Slots G2/G3 use seed namespaces 9,500,000/9,750,000.

### 7.8 Worker H -- High Band 80-89 Large-Scale (`worker_h.py`)

Generates permutations using an aggressive displacement-maximising strategy: for
each position (processed in shuffled order), the output value is chosen randomly
from the **top quarter** of remaining unused values by ring distance. This forces
mean ring distances well above 25 on every seed, reliably producing scores in the
80-89 band with a >99% hit rate and a vast design space (billions of distinct
rotation-key-unique permutations).

Typical score breakdown per permutation:

- **C1** ~ 24-27 (high ring displacement)
- **C2** ~ 18-20 (near-derangement; very few fixed points)
- **C3** ~ 5-8 (diverse cycle lengths from random assignment)
- **C4** ~ 15-20 (no structured runs)
- **C5** ~ 12-18 (uniform: 10th-percentile ring distance stays high)
- **Total** ~ 82-88

Seed namespace: 10,000,000+. Slots H2/H3/H4 use seed namespaces 11M/12M/13M.

### 7.9 Orchestrator (`orchestrator.py`)

Runs any combination of workers continuously in parallel threads until either all
workers have hit a consecutive-duplicate threshold or the database reaches a size
limit. State is persisted in a `worker_state` table in the same database so runs
can be safely interrupted and resumed.

```powershell
cd src\Data\configurations\workers

# Default: run all four original workers
python -u orchestrator.py

# Target-fill the 20-29 band
python -u orchestrator.py --workers F,F2,F3,A

# Target-fill the 80-89 band (Worker H -- large design space)
python -u orchestrator.py --workers H,H2,H3,H4

# Balanced run across all bands
python -u orchestrator.py --workers A,B,C,D,E,F,H
```

| Flag | Default | Description |
| --- | --- | --- |
| `--workers X,Y,...` | `A,B,C,D` | Comma-separated worker IDs to run in this session |
| `WORKER=seed` | (from registry) | Override starting seed for a specific worker slot |

**Registered worker slots:**

| Slot | Worker type | Default seed |
| --- | --- | --- |
| A | worker_a | 0 |
| B | worker_b | 1,000,000 |
| C | worker_c | 2,000,000 |
| D | worker_d | 3,000,000 |
| E | worker_e | 4,000,000 |
| E2 | worker_e | 5,000,000 |
| E3 | worker_e | 6,000,000 |
| E4 | worker_e | 7,000,000 |
| F | worker_f | 8,000,000 |
| F2 | worker_f | 8,500,000 |
| F3 | worker_f | 8,750,000 |
| G | worker_g | 9,000,000 |
| G2 | worker_g | 9,500,000 |
| G3 | worker_g | 9,750,000 |
| H | worker_h | 10,000,000 |
| H2 | worker_h | 11,000,000 |
| H3 | worker_h | 12,000,000 |
| H4 | worker_h | 13,000,000 |

---

## 8. Agent Prompts

Use these prompts to launch each worker as a background agent via the GitHub Copilot CLI.

**Before using any prompt:**

1. Copy the mandatory preamble block verbatim from `.copilot/directives/septenary.md` and
   paste it at the very start of the prompt, before the worker-specific content below.
2. Replace `[SEED_START]` with the `next_seed` value reported at the end of the previous
   batch run (or use the default seed from Section 7 for the first batch of each worker).

### 8.1 Worker A Prompt

```text
[Paste mandatory preamble from .copilot/directives/septenary.md here]

---

You are Worker A in the rotor configuration generation pipeline for the Enigma-NG project.

CONTEXT:
- Purpose: generating permutation wiring maps for base-64 Enigma-NG rotors
- Database: src/Data/configurations/rotor_configurations.db (SQLite)
- Scripts:  src/Data/configurations/workers/
- Process:  src/Data/configurations/rotor_configurations.md (Sections 4-7)

YOUR TASK:
Run one batch of Worker A (low-displacement bias, ~5-50 score range) to generate
approximately 100 new permutations.

1. Change directory to src/Data/configurations/workers/
2. Run: python worker_a.py [SEED_START] 100
3. Wait for the script to complete.

REPORT BACK the following (do not proceed further after the script finishes):
- Number of rows inserted
- Number of rows skipped (duplicates)
- Score distribution of inserted rows: min, max, and mean score_total
- The next_seed value printed on completion
- Any errors or exceptions encountered

RESTRICTIONS: Do NOT modify any source files. Do NOT run any other scripts.
Do NOT perform any git operations.
```

### 8.2 Worker B Prompt

```text
[Paste mandatory preamble from .copilot/directives/septenary.md here]

---

You are Worker B in the rotor configuration generation pipeline for the Enigma-NG project.

CONTEXT:
- Purpose: generating permutation wiring maps for base-64 Enigma-NG rotors
- Database: src/Data/configurations/rotor_configurations.db (SQLite)
- Scripts:  src/Data/configurations/workers/
- Process:  src/Data/configurations/rotor_configurations.md (Sections 4-7)

YOUR TASK:
Run one batch of Worker B (high-displacement bias, ~55-90 score range) to generate
approximately 100 new permutations.

1. Change directory to src/Data/configurations/workers/
2. Run: python worker_b.py [SEED_START] 100
3. Wait for the script to complete.

REPORT BACK the following (do not proceed further after the script finishes):
- Number of rows inserted
- Number of rows skipped (duplicates)
- Score distribution of inserted rows: min, max, and mean score_total
- The next_seed value printed on completion
- Any errors or exceptions encountered

RESTRICTIONS: Do NOT modify any source files. Do NOT run any other scripts.
Do NOT perform any git operations.
```

### 8.3 Worker C Prompt

```text
[Paste mandatory preamble from .copilot/directives/septenary.md here]

---

You are Worker C in the rotor configuration generation pipeline for the Enigma-NG project.

CONTEXT:
- Purpose: generating permutation wiring maps for base-64 Enigma-NG rotors
- Database: src/Data/configurations/rotor_configurations.db (SQLite)
- Scripts:  src/Data/configurations/workers/
- Process:  src/Data/configurations/rotor_configurations.md (Sections 4-7)

YOUR TASK:
Run one batch of Worker C (pure random, broad distribution) to generate approximately
100 new permutations.

1. Change directory to src/Data/configurations/workers/
2. Run: python worker_c.py [SEED_START] 100
3. Wait for the script to complete.

REPORT BACK the following (do not proceed further after the script finishes):
- Number of rows inserted
- Number of rows skipped (duplicates)
- Score distribution of inserted rows: min, max, and mean score_total
- The next_seed value printed on completion
- Any errors or exceptions encountered

RESTRICTIONS: Do NOT modify any source files. Do NOT run any other scripts.
Do NOT perform any git operations.
```

### 8.4 Worker D Prompt

```text
[Paste mandatory preamble from .copilot/directives/septenary.md here]

---

You are Worker D in the rotor configuration generation pipeline for the Enigma-NG project.

CONTEXT:
- Purpose: generating permutation wiring maps for base-64 Enigma-NG rotors
- Database: src/Data/configurations/rotor_configurations.db (SQLite)
- Scripts:  src/Data/configurations/workers/
- Process:  src/Data/configurations/rotor_configurations.md (Sections 4-7)

YOUR TASK:
Run one batch of Worker D (displacement-maximising, ~60-95 score range) to generate
approximately 100 new permutations.

1. Change directory to src/Data/configurations/workers/
2. Run: python worker_d.py [SEED_START] 100
3. Wait for the script to complete.

REPORT BACK the following (do not proceed further after the script finishes):
- Number of rows inserted
- Number of rows skipped (duplicates)
- Score distribution of inserted rows: min, max, and mean score_total
- The next_seed value printed on completion
- Any errors or exceptions encountered

RESTRICTIONS: Do NOT modify any source files. Do NOT run any other scripts.
Do NOT perform any git operations.
```

### 8.5 Worker E Prompt

```text
[Paste mandatory preamble from .copilot/directives/septenary.md here]

---

You are Worker E in the rotor configuration generation pipeline for the Enigma-NG project.

CONTEXT:
- Purpose: generating permutation wiring maps for base-64 Enigma-NG rotors
- Database: src/Data/configurations/rotor_configurations.db (SQLite)
- Scripts:  src/Data/configurations/workers/
- Process:  src/Data/configurations/rotor_configurations.md (Sections 4-7)

YOUR TASK:
Run one batch of Worker E (stride-swap band-filler, 30-49 score range) to generate
approximately 100 new permutations.

1. Change directory to src/Data/configurations/workers/
2. Run: python worker_e.py [SEED_START] 100
3. Wait for the script to complete.

REPORT BACK the following (do not proceed further after the script finishes):
- Number of rows inserted
- Number of rows skipped (duplicates)
- Score distribution of inserted rows: min, max, and mean score_total
- The next_seed value printed on completion
- Any errors or exceptions encountered

RESTRICTIONS: Do NOT modify any source files. Do NOT run any other scripts.
Do NOT perform any git operations.
```

### 8.6 Worker F Prompt

```text
[Paste mandatory preamble from .copilot/directives/septenary.md here]

---

You are Worker F in the rotor configuration generation pipeline for the Enigma-NG project.

CONTEXT:
- Purpose: generating permutation wiring maps for base-64 Enigma-NG rotors
- Database: src/Data/configurations/rotor_configurations.db (SQLite)
- Scripts:  src/Data/configurations/workers/
- Process:  src/Data/configurations/rotor_configurations.md (Sections 4-7)

YOUR TASK:
Run one batch of Worker F (partial Fisher-Yates, 20-29 score range) to generate
approximately 100 new permutations.

1. Change directory to src/Data/configurations/workers/
2. Run: python worker_f.py [SEED_START] 100
3. Wait for the script to complete.

REPORT BACK the following (do not proceed further after the script finishes):
- Number of rows inserted
- Number of rows skipped (duplicates)
- Score distribution of inserted rows: min, max, and mean score_total
- The next_seed value printed on completion
- Any errors or exceptions encountered

RESTRICTIONS: Do NOT modify any source files. Do NOT run any other scripts.
Do NOT perform any git operations.
```

### 8.7 Worker G Prompt

```text
[Paste mandatory preamble from .copilot/directives/septenary.md here]

---

You are Worker G in the rotor configuration generation pipeline for the Enigma-NG project.

CONTEXT:
- Purpose: generating permutation wiring maps for base-64 Enigma-NG rotors
- Database: src/Data/configurations/rotor_configurations.db (SQLite)
- Scripts:  src/Data/configurations/workers/
- Process:  src/Data/configurations/rotor_configurations.md (Sections 4-7)

YOUR TASK:
Run one batch of Worker G (shift-by-32 pair-swap, 80-89 score range) to generate
approximately 100 new permutations.

1. Change directory to src/Data/configurations/workers/
2. Run: python worker_g.py [SEED_START] 100
3. Wait for the script to complete.

REPORT BACK the following (do not proceed further after the script finishes):
- Number of rows inserted
- Number of rows skipped (duplicates)
- Score distribution of inserted rows: min, max, and mean score_total
- The next_seed value printed on completion
- Any errors or exceptions encountered

RESTRICTIONS: Do NOT modify any source files. Do NOT run any other scripts.
Do NOT perform any git operations.
```

### 8.8 Worker H Prompt

```text
[Paste mandatory preamble from .copilot/directives/septenary.md here]

---

You are Worker H in the rotor configuration generation pipeline for the Enigma-NG project.

CONTEXT:
- Purpose: generating permutation wiring maps for base-64 Enigma-NG rotors
- Database: src/Data/configurations/rotor_configurations.db (SQLite)
- Scripts:  src/Data/configurations/workers/
- Process:  src/Data/configurations/rotor_configurations.md (Sections 4-7)

YOUR TASK:
Run one batch of Worker H (top-quarter displacement-maximising, 80-89 score range) to generate
approximately 100 new permutations. Worker H has a very large design space (billions of unique
rotation keys) and a >99% hit rate in the 80-89 band.

1. Change directory to src/Data/configurations/workers/
2. Run: python worker_h.py [SEED_START] 100
3. Wait for the script to complete.

REPORT BACK the following (do not proceed further after the script finishes):
- Number of rows inserted
- Number of rows skipped (duplicates)
- Score distribution of inserted rows: min, max, and mean score_total
- The next_seed value printed on completion
- Any errors or exceptions encountered

RESTRICTIONS: Do NOT modify any source files. Do NOT run any other scripts.
Do NOT perform any git operations.
```