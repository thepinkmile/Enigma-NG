"""Band distribution monitor and automatic worker rotation.

Polls band statistics every POLL_INTERVAL seconds, calculates which bands are
most under-represented relative to the current total, selects the optimal set
of worker slots to address the deficit, and restarts the orchestrator whenever
the optimal set differs from the currently running set.

Bands 30-49 are treated as "saturated cap" bands -- they are excluded from the
deficit calculation and no workers that exclusively target them are ever selected.
Workers B, C, D produce a broad range including 50-89; they are assigned to
whichever of those sub-bands is most deficient.

Usage:
    python -u band_monitor.py [--slots N] [--interval S]
                              [--focus-band B] [--target-count T]

  --slots N       Number of parallel worker slots to run (default: 4)
  --interval S    Seconds between band polls (default: 90)
  --focus-band B  Lock all slots onto this score band (e.g. 80 for 80-89)
  --target-count T  Stop when the focus band reaches T unique rows
"""

import os
import signal
import sqlite3
import subprocess
import sys
import time
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from worker_utils import get_db_path  # noqa: E402

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

POLL_INTERVAL = 90       # seconds between stat checks
WORKER_SLOTS  = 4        # number of parallel orchestrator worker slots
LOG_FILE      = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              'band_monitor.log')

# Bands we actively try to fill (0-indexed by band floor).
# Bands 30-49 are excluded -- already heavily saturated.
TARGET_BANDS = [0, 10, 20, 50, 60, 70, 80]

# Band → candidate worker slots, in priority order.
# Listed in approximate effectiveness order; first slot tried first.
BAND_WORKERS = {
    0:  ['A', 'A2', 'A3'],
    10: ['A', 'A2', 'A3'],
    20: ['F', 'F2', 'F3'],
    50: ['B', 'C',  'D',  'B2', 'C2', 'D2'],
    60: ['C', 'B',  'D',  'C2', 'B2', 'D2'],
    70: ['D', 'C',  'B',  'D2', 'C2', 'B2'],
    80: ['H', 'H2', 'H3', 'H4', 'G', 'G2', 'G3'],
}

# Worker slots that are known to have near-exhausted their seed space
# (>90% skip rate sustained over 3 consecutive polls) are added here
# automatically and avoided in future selection.
_exhausted: set = set()

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _ts() -> str:
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def _log(msg: str):
    line = f"[{_ts()}] {msg}"
    print(line, flush=True)
    with open(LOG_FILE, 'a') as f:
        f.write(line + '\n')


def _get_band_counts() -> dict:
    """Return {band_floor: count} for all rows with a non-NULL score."""
    try:
        conn = sqlite3.connect(get_db_path(), timeout=10)
        rows = conn.execute("""
            SELECT CAST(score_total / 10 AS INT) * 10 AS band, COUNT(*) AS cnt
            FROM rotor_configurations
            WHERE score_total IS NOT NULL
            GROUP BY band
        """).fetchall()
        conn.close()
        return {r[0]: r[1] for r in rows}
    except Exception as e:
        _log(f"DB query error: {e}")
        return {}


def _get_worker_skip_rates(active_workers: list) -> dict:
    """Return {worker_id: consecutive_fail_count} from worker_state."""
    try:
        conn = sqlite3.connect(get_db_path(), timeout=10)
        placeholders = ','.join('?' * len(active_workers))
        rows = conn.execute(
            f"SELECT worker_id, consecutive_fails FROM worker_state "
            f"WHERE worker_id IN ({placeholders})",
            active_workers,
        ).fetchall()
        conn.close()
        return {r[0]: r[1] for r in rows}
    except Exception:
        return {}


def _choose_workers(band_counts: dict, n_slots: int) -> list:
    """Select the best n_slots worker IDs to address current band deficits."""
    total = sum(band_counts.get(b, 0) for b in TARGET_BANDS)
    if total == 0:
        return ['A', 'F', 'B', 'G'][:n_slots]

    # Calculate deficit for each target band (how far below equal share it is)
    equal_share = total / len(TARGET_BANDS)
    deficits = {
        band: max(0, equal_share - band_counts.get(band, 0))
        for band in TARGET_BANDS
    }

    # Sort bands by deficit descending
    priority_bands = sorted(deficits, key=lambda b: deficits[b], reverse=True)

    selected = []
    used_slots: set = set()  # avoid selecting the same slot twice

    for band in priority_bands:
        if len(selected) >= n_slots:
            break
        for worker in BAND_WORKERS.get(band, []):
            if worker not in used_slots and worker not in _exhausted:
                selected.append(worker)
                used_slots.add(worker)
                break  # one slot per band per pass

    # If we still have slots left, fill with any available worker
    if len(selected) < n_slots:
        for band in priority_bands:
            for worker in BAND_WORKERS.get(band, []):
                if worker not in used_slots and worker not in _exhausted:
                    selected.append(worker)
                    used_slots.add(worker)
                if len(selected) >= n_slots:
                    break
            if len(selected) >= n_slots:
                break

    return selected[:n_slots]


def _format_distribution(band_counts: dict) -> str:
    total = sum(band_counts.values())
    lines = [f"Total: {total:,}"]
    for band in sorted(set(band_counts) | set(TARGET_BANDS)):
        cnt   = band_counts.get(band, 0)
        pct   = 100 * cnt / total if total else 0
        mark  = ' *' if band in TARGET_BANDS else ''
        lines.append(f"  {band:3d}-{band+9:3d}  {cnt:>10,}  {pct:5.1f}%{mark}")
    return '\n'.join(lines)


# ---------------------------------------------------------------------------
# Orchestrator subprocess management
# ---------------------------------------------------------------------------

_orch_proc = None
_current_workers: list = []


def _start_orchestrator(workers: list):
    global _orch_proc, _current_workers
    log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            'orchestrator_monitor.log')
    _log(f"Starting orchestrator with workers: {', '.join(workers)}")
    _orch_proc = subprocess.Popen(
        [sys.executable, '-u', 'orchestrator.py', '--workers', ','.join(workers)],
        cwd=os.path.dirname(os.path.abspath(__file__)),
        stdout=open(log_path, 'a'),
        stderr=subprocess.STDOUT,
    )
    _current_workers = workers[:]
    _log(f"Orchestrator PID {_orch_proc.pid}")


def _stop_orchestrator():
    global _orch_proc
    if _orch_proc and _orch_proc.poll() is None:
        _log(f"Stopping orchestrator PID {_orch_proc.pid}")
        _orch_proc.terminate()
        try:
            _orch_proc.wait(timeout=15)
        except subprocess.TimeoutExpired:
            _orch_proc.kill()
        _orch_proc = None


def _check_exhaustion(active_workers: list):
    """Mark workers with high consecutive_fails as exhausted."""
    skip_rates = _get_worker_skip_rates(active_workers)
    for wid, cf in skip_rates.items():
        if cf >= 10 and wid not in _exhausted:
            _log(f"Worker {wid} marked exhausted (consecutive_fails={cf})")
            _exhausted.add(wid)


# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------

def main(n_slots: int = WORKER_SLOTS, poll_interval: int = POLL_INTERVAL,
         focus_band: int = None, target_count: int = None):
    _log("=" * 60)
    msg = f"Band monitor starting  slots={n_slots}  interval={poll_interval}s"
    if focus_band is not None:
        msg += f"  FOCUSED on band {focus_band}-{focus_band+9}"
    if target_count is not None:
        msg += f"  target_count={target_count:,}"
    _log(msg)
    _log("=" * 60)

    # Handle Ctrl-C gracefully
    def _shutdown(sig, frame):
        _log("Shutdown signal received.")
        _stop_orchestrator()
        sys.exit(0)
    signal.signal(signal.SIGINT, _shutdown)
    signal.signal(signal.SIGTERM, _shutdown)

    poll_num = 0

    while True:
        poll_num += 1
        band_counts = _get_band_counts()

        if band_counts:
            _log(f"--- Poll {poll_num} ---")
            _log(_format_distribution(band_counts))

            # Check focused-band target stop condition
            if focus_band is not None and target_count is not None:
                current = band_counts.get(focus_band, 0)
                _log(f"Band {focus_band}-{focus_band+9}: {current:,} / {target_count:,}")
                if current >= target_count:
                    _log(f"Target reached ({current:,} >= {target_count:,}). Stopping.")
                    _stop_orchestrator()
                    sys.exit(0)

            # Mark any currently active workers as exhausted if applicable
            if _current_workers:
                _check_exhaustion(_current_workers)

            # In focused mode, only select workers for the target band
            if focus_band is not None:
                available = [
                    w for w in BAND_WORKERS.get(focus_band, [])
                    if w not in _exhausted
                ]
                optimal = available[:n_slots]
                if not optimal:
                    _log(f"All workers for band {focus_band} exhausted. Stopping.")
                    _stop_orchestrator()
                    sys.exit(0)
            else:
                optimal = _choose_workers(band_counts, n_slots)

            if set(optimal) != set(_current_workers):
                _log(f"Worker set change: {_current_workers} -> {optimal}")
                _stop_orchestrator()
                _start_orchestrator(optimal)
            else:
                # Check if orchestrator died unexpectedly
                if _orch_proc and _orch_proc.poll() is not None:
                    _log("Orchestrator exited unexpectedly; restarting.")
                    _start_orchestrator(_current_workers)
                else:
                    _log(f"Workers unchanged: {', '.join(_current_workers)}")
        else:
            _log("No band data available yet.")
            if not _orch_proc or _orch_proc.poll() is not None:
                initial = ['F', 'F2', 'A', 'G'][:n_slots]
                _start_orchestrator(initial)

        time.sleep(poll_interval)


if __name__ == '__main__':
    slots        = WORKER_SLOTS
    interval     = POLL_INTERVAL
    focus_band   = None
    target_count = None
    for arg in sys.argv[1:]:
        if arg.startswith('--slots='):
            slots = int(arg.split('=', 1)[1])
        elif arg.startswith('--interval='):
            interval = int(arg.split('=', 1)[1])
        elif arg.startswith('--focus-band='):
            focus_band = int(arg.split('=', 1)[1])
        elif arg.startswith('--target-count='):
            target_count = int(arg.split('=', 1)[1])
    main(slots, interval, focus_band=focus_band, target_count=target_count)
