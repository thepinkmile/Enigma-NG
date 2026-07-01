"""Orchestrator: runs configurable workers in continuous rounds.

Termination conditions (whichever comes first):
  1. ALL workers have accumulated FAIL_THRESHOLD consecutive batches in which
     every seed produced a duplicate (inserted == 0).  A worker that reaches
     this threshold is marked "done" but continues running until every other
     worker is also done -- this prevents a fast-exhausting worker from
     starving the others of their fair run.
  2. The database file size exceeds MAX_DB_GB gigabytes.

State (current seed, batch counts, consecutive-fail counter) is persisted in
a worker_state table inside the same SQLite database so the run can be safely
interrupted and restarted without losing progress.

Usage:
    python orchestrator.py [--workers A,B,C,D] [WORKER=seed ...]

  --workers   Comma-separated list of worker IDs to run in this session.
              Available IDs: A B C D E E2 E3 E4
              Default: A,B,C,D

  WORKER=seed Seed override for first-time initialisation of a worker slot,
              e.g. A=59206 B=1057239.  Ignored if the slot already has a
              saved state row.

Examples:
    python orchestrator.py                        # default ABCD
    python orchestrator.py --workers A,E,E2,E3    # focus on 30-49 band
    python orchestrator.py --workers E,E2,E3,E4   # all-E saturation run
"""

import os
import sys
import threading
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from worker_utils import (  # noqa: E402
    get_connection,
    get_db_path,
    run_seeded_batch,
)
import worker_a  # noqa: E402
import worker_b  # noqa: E402
import worker_c  # noqa: E402
import worker_d  # noqa: E402
import worker_e  # noqa: E402
import worker_f  # noqa: E402
import worker_g  # noqa: E402
import worker_h  # noqa: E402

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

BATCH_SEEDS    = 1_000       # seeds processed per batch
FAIL_THRESHOLD = 3           # consecutive all-duplicate batches to declare "done"
MAX_DB_GB      = 300         # stop if DB file exceeds this many gigabytes
MAX_DB_BYTES   = MAX_DB_GB * (1024 ** 3)

# ---------------------------------------------------------------------------
# Worker registry  -- add new worker types here
# ---------------------------------------------------------------------------

_WORKER_REGISTRY = {
    'A':  {'generate': worker_a.generate, 'default_seed':          0},
    'A2': {'generate': worker_a.generate, 'default_seed':    500_000},
    'A3': {'generate': worker_a.generate, 'default_seed':    750_000},
    'B':  {'generate': worker_b.generate, 'default_seed':  1_000_000},
    'B2': {'generate': worker_b.generate, 'default_seed':  1_500_000},
    'C':  {'generate': worker_c.generate, 'default_seed':  2_000_000},
    'C2': {'generate': worker_c.generate, 'default_seed':  2_500_000},
    'D':  {'generate': worker_d.generate, 'default_seed':  3_000_000},
    'D2': {'generate': worker_d.generate, 'default_seed':  3_500_000},
    'E':  {'generate': worker_e.generate, 'default_seed':  4_000_000},
    'E2': {'generate': worker_e.generate, 'default_seed':  5_000_000},
    'E3': {'generate': worker_e.generate, 'default_seed':  6_000_000},
    'E4': {'generate': worker_e.generate, 'default_seed':  7_000_000},
    'F':  {'generate': worker_f.generate, 'default_seed':  8_000_000},
    'F2': {'generate': worker_f.generate, 'default_seed':  8_500_000},
    'F3': {'generate': worker_f.generate, 'default_seed':  8_750_000},
    'G':  {'generate': worker_g.generate, 'default_seed':  9_000_000},
    'G2': {'generate': worker_g.generate, 'default_seed':  9_500_000},
    'G3': {'generate': worker_g.generate, 'default_seed':  9_750_000},
    'H':  {'generate': worker_h.generate, 'default_seed': 10_000_000},
    'H2': {'generate': worker_h.generate, 'default_seed': 11_000_000},
    'H3': {'generate': worker_h.generate, 'default_seed': 12_000_000},
    'H4': {'generate': worker_h.generate, 'default_seed': 13_000_000},
}

# ---------------------------------------------------------------------------
# worker_state table
# ---------------------------------------------------------------------------

_CREATE_STATE_TABLE = """
CREATE TABLE IF NOT EXISTS worker_state (
    worker_id         TEXT    PRIMARY KEY,
    current_seed      INTEGER NOT NULL,
    batches_run       INTEGER DEFAULT 0,
    consecutive_fails INTEGER DEFAULT 0,
    is_done           INTEGER DEFAULT 0,
    total_inserted    INTEGER DEFAULT 0,
    total_skipped     INTEGER DEFAULT 0,
    last_updated      TEXT    DEFAULT NULL
)
"""


def _ensure_state_table(conn, active_workers: list, seed_overrides: dict):
    conn.execute(_CREATE_STATE_TABLE)
    for wid in active_workers:
        seed = seed_overrides.get(wid, _WORKER_REGISTRY[wid]['default_seed'])
        conn.execute(
            "INSERT OR IGNORE INTO worker_state (worker_id, current_seed) VALUES (?, ?)",
            (wid, seed),
        )


def _load_state(conn, active_workers: list) -> dict:
    placeholders = ','.join('?' * len(active_workers))
    rows = conn.execute(
        f"SELECT worker_id, current_seed, batches_run, consecutive_fails, "
        f"is_done, total_inserted, total_skipped FROM worker_state "
        f"WHERE worker_id IN ({placeholders})",
        active_workers,
    ).fetchall()
    return {
        r[0]: {
            'seed':              r[1],
            'batches_run':       r[2],
            'consecutive_fails': r[3],
            'is_done':           bool(r[4]),
            'total_inserted':    r[5],
            'total_skipped':     r[6],
        }
        for r in rows
    }


def _save_state(conn, wid: str, s: dict):
    conn.execute(
        "UPDATE worker_state SET current_seed=?, batches_run=?, consecutive_fails=?, "
        "is_done=?, total_inserted=?, total_skipped=?, last_updated=? "
        "WHERE worker_id=?",
        (
            s['seed'], s['batches_run'], s['consecutive_fails'],
            int(s['is_done']), s['total_inserted'], s['total_skipped'],
            datetime.now(timezone.utc).isoformat(), wid,
        ),
    )


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _db_bytes() -> int:
    try:
        return os.path.getsize(get_db_path())
    except OSError:  # pragma: no cover — only reachable if the DB file has never been created
        return 0


def _db_row_count(conn) -> int:
    return conn.execute("SELECT COUNT(*) FROM rotor_configurations").fetchone()[0]


# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------

def main(active_workers: list, seed_overrides: dict = None,
         max_rounds: int = None, conn_factory=None):
    overrides = seed_overrides or {}
    _get_conn = conn_factory or get_connection
    unknown = [w for w in active_workers if w not in _WORKER_REGISTRY]
    if unknown:
        print(f"Unknown worker ID(s): {', '.join(unknown)}")
        print(f"Available: {', '.join(_WORKER_REGISTRY)}")
        sys.exit(1)

    conn = _get_conn()
    _ensure_state_table(conn, active_workers, overrides)
    state = _load_state(conn, active_workers)
    conn.close()

    print(f"Orchestrator starting")
    print(f"  Workers: {', '.join(active_workers)}")
    print(f"  BATCH_SEEDS={BATCH_SEEDS}  FAIL_THRESHOLD={FAIL_THRESHOLD}  MAX_DB={MAX_DB_GB} GB")
    print(f"  Starting seeds: " + "  ".join(f"{w}={state[w]['seed']:,}" for w in active_workers))
    print()

    round_num = 0

    while True:
        round_num += 1

        # ---- max_rounds guard (used in tests) --------------------------------
        if max_rounds is not None and round_num > max_rounds:
            break

        # ---- DB size check ---------------------------------------------------
        db_bytes = _db_bytes()
        if db_bytes >= MAX_DB_BYTES:
            print(f"\n[!] DB size limit reached ({db_bytes / (1024**3):.2f} GB). Stopping.")
            break

        # ---- Global termination check ----------------------------------------
        if all(state[w]['is_done'] for w in active_workers):
            print("\n[!] All workers have hit the consecutive-duplicate threshold. Stopping.")
            break

        # ---- Run one batch per worker in parallel ----------------------------
        batch_results: dict = {}
        lock = threading.Lock()

        def _thread(wid, generate_fn, seed, seed_count, cf):
            conn = cf()
            ins, skp, next_seed = run_seeded_batch(generate_fn, seed, seed_count, conn)
            conn.close()
            with lock:
                batch_results[wid] = (ins, skp, next_seed)

        threads = [
            threading.Thread(
                target=_thread,
                args=(wid, _WORKER_REGISTRY[wid]['generate'], state[wid]['seed'], BATCH_SEEDS,
                      _get_conn),
            )
            for wid in active_workers
        ]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        # ---- Update and persist state ----------------------------------------
        conn = _get_conn()
        newly_done = []
        for wid in active_workers:
            ins, skp, next_seed = batch_results[wid]
            s = state[wid]
            s['seed']            = next_seed
            s['batches_run']    += 1
            s['total_inserted'] += ins
            s['total_skipped']  += skp

            if ins == 0:
                s['consecutive_fails'] += 1
            else:
                s['consecutive_fails'] = 0

            if s['consecutive_fails'] >= FAIL_THRESHOLD and not s['is_done']:
                s['is_done'] = True
                newly_done.append(wid)

            _save_state(conn, wid, s)

        total_rows = _db_row_count(conn)
        conn.close()

        # ---- Progress report -------------------------------------------------
        round_ins  = sum(batch_results[w][0] for w in active_workers)
        round_skp  = sum(batch_results[w][1] for w in active_workers)
        total_seen = round_ins + round_skp
        skip_pct   = 100 * round_skp // total_seen if total_seen else 0
        db_mb      = db_bytes / (1024 ** 2)
        done_flags = '[' + ''.join(w if state[w]['is_done'] else '.' for w in active_workers) + ']'

        print(
            f"Round {round_num:>6,}  |  rows={total_rows:>9,}  "
            f"ins={round_ins:>5}  skp={round_skp:>5}  skip%={skip_pct:>3}%  "
            f"db={db_mb:>8.1f}MB  done={done_flags}"
        )
        for wid in active_workers:
            ins, skp, _ = batch_results[wid]
            s = state[wid]
            cf_str   = f"  consec_fails={s['consecutive_fails']}" if s['consecutive_fails'] else ""
            done_str = "  *** DONE ***" if wid in newly_done else ""
            print(
                f"  [{wid:>2}]  ins={ins:>4}  skp={skp:>4}  "
                f"next_seed={s['seed']:>12,}{cf_str}{done_str}"
            )

        if newly_done:
            remaining = [w for w in active_workers if not state[w]['is_done']]
            if remaining:
                print(f"  [!] Worker(s) {', '.join(newly_done)} reached fail threshold. "
                      f"Waiting for: {', '.join(remaining)}")

    # ---- Final summary -------------------------------------------------------
    print("\n=== Final Summary ===")
    conn = _get_conn()
    total_rows = _db_row_count(conn)
    conn.close()
    print(f"Total rows in DB: {total_rows:,}")
    for wid in active_workers:
        s = state[wid]
        print(
            f"  [{wid:>2}]  inserted={s['total_inserted']:>10,}  "
            f"skipped={s['total_skipped']:>10,}  "
            f"next_seed={s['seed']:>12,}  "
            f"batches={s['batches_run']:>6,}"
        )


if __name__ == '__main__':  # pragma: no cover
    workers_arg = 'A,B,C,D'
    overrides = {}

    argv = sys.argv[1:]
    i = 0
    while i < len(argv):
        arg = argv[i]
        if arg == '--workers' and i + 1 < len(argv):
            workers_arg = argv[i + 1]
            i += 2
        elif arg.startswith('--workers='):
            workers_arg = arg.split('=', 1)[1]
            i += 1
        elif '=' in arg and not arg.startswith('--'):
            wid, seed = arg.split('=', 1)
            overrides[wid.upper()] = int(seed)
            i += 1
        else:
            i += 1

    active = [w.strip().upper() for w in workers_arg.split(',')]
    main(active, overrides or None)
