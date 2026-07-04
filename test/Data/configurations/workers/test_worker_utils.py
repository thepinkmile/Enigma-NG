"""Unit tests for worker_utils.py.

Tests cover ring_dist, make_rotation_key, claim_permutation (including
concurrency), update_scores, and compute_score. Duplicate-detection tests
explicitly verify that rotations and element-wise reversals of a claimed
permutation are all rejected.

Each test class that touches the database creates its own in-memory (or
temp-file) SQLite DB with the exact production schema so no production data
is ever touched or mutated.
"""

import os
import sqlite3
import sys
import tempfile
import threading
import unittest

import importlib

# Resolve the source workers directory relative to this file's location so
# worker_utils can be imported regardless of where pytest is invoked from.
# Layout: test/Data/configurations/workers/ -> up 4 -> src/Data/configurations/workers/
_WORKERS_SRC = os.path.normpath(
    os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        '..', '..', '..', '..', 'src', 'Data', 'configurations', 'workers',
    )
)
sys.path.insert(0, _WORKERS_SRC)

from worker_utils import (  # noqa: E402
    N,
    claim_permutation,
    compute_score,
    make_rotation_key,
    ring_dist,
    run_seeded_batch,
    update_scores,
)

import worker_e          # noqa: E402
import worker_f          # noqa: E402
import worker_g          # noqa: E402
import worker_h          # noqa: E402
import orchestrator      # noqa: E402

# ---------------------------------------------------------------------------
# Schema - mirrors the production DB exactly.
# ---------------------------------------------------------------------------

_P_COLS = ', '.join(f'p{i} INTEGER' for i in range(N))

_CREATE_TABLE = f"""
CREATE TABLE IF NOT EXISTS rotor_configurations (
    id                    INTEGER PRIMARY KEY AUTOINCREMENT,
    reflected_index       INTEGER DEFAULT NULL,
    notes                 TEXT    DEFAULT NULL,
    {_P_COLS},
    score_total           REAL    DEFAULT NULL,
    score_c1_displacement REAL    DEFAULT NULL,
    score_c2_fixed_points REAL    DEFAULT NULL,
    fixed_point_count     INTEGER DEFAULT NULL,
    score_c3_cycles       REAL    DEFAULT NULL,
    score_c4_runs         REAL    DEFAULT NULL,
    score_c5_uniformity   REAL    DEFAULT NULL,
    selected              INTEGER DEFAULT 0,
    rotation_key          TEXT    DEFAULT NULL
)
"""

_CREATE_INDEX = (
    "CREATE INDEX IF NOT EXISTS idx_rotation_key "
    "ON rotor_configurations (rotation_key)"
)


def _make_connection(db_path: str = ':memory:') -> sqlite3.Connection:
    """Open a connection with the production schema in autocommit mode.

    Passing db_path=':memory:' (the default) creates a fresh, isolated
    in-memory database suitable for sequential tests. Pass a temp-file path
    when two separate connections need to share the same database (e.g. for
    concurrency tests).
    """
    conn = sqlite3.connect(db_path, timeout=30, check_same_thread=False)
    conn.isolation_level = None  # autocommit - required for BEGIN IMMEDIATE
    conn.execute(_CREATE_TABLE)
    conn.execute(_CREATE_INDEX)
    return conn


# ---------------------------------------------------------------------------
# Permutation helpers
# ---------------------------------------------------------------------------

def _seeded_perm(seed: int) -> list:
    """Deterministic random permutation of 0..N-1 from a fixed seed."""
    import random
    p = list(range(N))
    random.Random(seed).shuffle(p)
    return p


def _pair_swap_perm() -> list:
    """[1,0,3,2,...,63,62] - every adjacent pair swapped, zero fixed points."""
    p = list(range(N))
    for i in range(0, N, 2):
        p[i], p[i + 1] = p[i + 1], p[i]
    return p


def _rotate(perm: list, k: int) -> list:
    """Cyclic left-shift: new[i] = perm[(i + k) % N]."""
    return [perm[(i + k) % N] for i in range(N)]


def _reverse(perm: list) -> list:
    return perm[::-1]


# ===========================================================================
# TestRingDist
# ===========================================================================

class TestRingDist(unittest.TestCase):

    def test_zero_distance(self):
        self.assertEqual(ring_dist(0, 0), 0)
        self.assertEqual(ring_dist(32, 32), 0)
        self.assertEqual(ring_dist(63, 63), 0)

    def test_max_distance(self):
        # Maximum ring distance on N=64 is 32 (diametrically opposite).
        self.assertEqual(ring_dist(0, 32), 32)
        self.assertEqual(ring_dist(16, 48), 32)
        self.assertEqual(ring_dist(1, 33), 32)

    def test_wrap_around(self):
        # 0 and 63 are adjacent on a ring of 64 positions (distance = 1).
        self.assertEqual(ring_dist(0, 63), 1)
        self.assertEqual(ring_dist(63, 0), 1)
        self.assertEqual(ring_dist(1, 63), 2)
        self.assertEqual(ring_dist(2, 63), 3)

    def test_symmetric(self):
        for a, b in [(5, 60), (0, 10), (20, 40), (0, 63), (1, 32)]:
            with self.subTest(a=a, b=b):
                self.assertEqual(ring_dist(a, b), ring_dist(b, a))

    def test_small_forward_distance(self):
        self.assertEqual(ring_dist(10, 15), 5)
        self.assertEqual(ring_dist(0, 1), 1)

    def test_wrap_beats_direct(self):
        # Going backward 14 steps is shorter than forward 50.
        self.assertEqual(ring_dist(0, 50), 14)


# ===========================================================================
# TestMakeRotationKey
# ===========================================================================

class TestMakeRotationKey(unittest.TestCase):

    def test_same_perm_same_key(self):
        p = _seeded_perm(42)
        self.assertEqual(make_rotation_key(p), make_rotation_key(p))

    def test_rotation_same_key(self):
        p = _seeded_perm(42)
        key = make_rotation_key(p)
        for k in [1, 2, 7, 15, 31, 32, 33, 63]:
            with self.subTest(k=k):
                self.assertEqual(make_rotation_key(_rotate(p, k)), key)

    def test_reverse_same_key(self):
        p = _seeded_perm(42)
        self.assertEqual(make_rotation_key(p), make_rotation_key(_reverse(p)))

    def test_rotation_of_reverse_same_key(self):
        p = _seeded_perm(42)
        key = make_rotation_key(p)
        rev = _reverse(p)
        for k in [1, 8, 16, 32, 63]:
            with self.subTest(k=k):
                self.assertEqual(make_rotation_key(_rotate(rev, k)), key)

    def test_unrelated_perms_different_keys(self):
        # Two independently seeded random permutations are essentially
        # never rotationally equivalent for N=64.
        p1 = _seeded_perm(0)
        p2 = _seeded_perm(1)
        self.assertNotEqual(make_rotation_key(p1), make_rotation_key(p2))

    def test_all_64_rotations_share_one_key(self):
        p = _seeded_perm(99)
        key = make_rotation_key(p)
        keys = {make_rotation_key(_rotate(p, k)) for k in range(N)}
        self.assertEqual(len(keys), 1)
        self.assertEqual(keys.pop(), key)

    def test_all_64_reverse_rotations_share_same_key(self):
        p = _seeded_perm(99)
        key = make_rotation_key(p)
        keys = {make_rotation_key(_rotate(_reverse(p), k)) for k in range(N)}
        self.assertEqual(len(keys), 1)
        self.assertEqual(keys.pop(), key)


# ===========================================================================
# TestClaimPermutation  (sequential, in-memory DB)
# ===========================================================================

class TestClaimPermutation(unittest.TestCase):

    def setUp(self):
        self.conn = _make_connection()

    def tearDown(self):
        self.conn.close()

    def _claim(self, perm: list):
        return claim_permutation(self.conn, perm, make_rotation_key(perm))

    # -- success path -------------------------------------------------------

    def test_first_claim_returns_positive_row_id(self):
        row_id = self._claim(_seeded_perm(42))
        self.assertIsNotNone(row_id)
        self.assertGreater(row_id, 0)

    def test_claimed_row_has_null_scores(self):
        row_id = self._claim(_seeded_perm(42))
        result = self.conn.execute(
            'SELECT score_total FROM rotor_configurations WHERE id = ?',
            (row_id,)
        ).fetchone()[0]
        self.assertIsNone(result)

    def test_row_count_after_single_claim(self):
        self._claim(_seeded_perm(42))
        count = self.conn.execute(
            'SELECT COUNT(*) FROM rotor_configurations'
        ).fetchone()[0]
        self.assertEqual(count, 1)

    def test_two_independent_perms_both_accepted(self):
        id1 = self._claim(_seeded_perm(42))
        id2 = self._claim(_seeded_perm(43))
        self.assertIsNotNone(id1)
        self.assertIsNotNone(id2)
        self.assertNotEqual(id1, id2)

    # -- exact-duplicate rejection ------------------------------------------

    def test_claim_first_succeeds_second_fails(self):
        """Claiming the same permutation twice: first must succeed, second must fail."""
        p = _seeded_perm(42)
        first = self._claim(p)
        second = self._claim(p)
        self.assertIsNotNone(first,  "First claim should return a row id")
        self.assertGreater(first, 0, "First claim row id should be positive")
        self.assertIsNone(second,    "Second claim of identical perm should be rejected")

    def test_same_perm_rejected(self):
        p = _seeded_perm(42)
        self._claim(p)
        self.assertIsNone(self._claim(p))

    # -- rotational-duplicate rejection -------------------------------------

    def test_rotation_by_1_rejected(self):
        p = _seeded_perm(42)
        self._claim(p)
        self.assertIsNone(self._claim(_rotate(p, 1)))

    def test_rotation_by_8_rejected(self):
        p = _seeded_perm(42)
        self._claim(p)
        self.assertIsNone(self._claim(_rotate(p, 8)))

    def test_rotation_by_32_rejected(self):
        p = _seeded_perm(42)
        self._claim(p)
        self.assertIsNone(self._claim(_rotate(p, 32)))

    def test_rotation_by_63_rejected(self):
        p = _seeded_perm(42)
        self._claim(p)
        self.assertIsNone(self._claim(_rotate(p, 63)))

    def test_all_64_rotations_rejected(self):
        p = _seeded_perm(42)
        self._claim(p)
        for k in range(1, N):
            with self.subTest(k=k):
                self.assertIsNone(self._claim(_rotate(p, k)))

    # -- reverse-duplicate rejection ----------------------------------------

    def test_reverse_rejected(self):
        p = _seeded_perm(42)
        self._claim(p)
        self.assertIsNone(self._claim(_reverse(p)))

    def test_rotation_of_reverse_rejected(self):
        p = _seeded_perm(42)
        self._claim(p)
        rev = _reverse(p)
        for k in [1, 8, 32, 63]:
            with self.subTest(k=k):
                self.assertIsNone(self._claim(_rotate(rev, k)))

    def test_all_64_reverse_rotations_rejected(self):
        p = _seeded_perm(42)
        self._claim(p)
        rev = _reverse(p)
        for k in range(N):
            with self.subTest(k=k):
                self.assertIsNone(self._claim(_rotate(rev, k)))

    def test_exactly_one_row_after_all_128_variants(self):
        """Claiming a perm and all 128 rotational/reverse variants leaves 1 row."""
        p = _seeded_perm(42)
        self._claim(p)
        rev = _reverse(p)
        for k in range(N):
            for src in (p, rev):
                self._claim(_rotate(src, k))
        count = self.conn.execute(
            'SELECT COUNT(*) FROM rotor_configurations'
        ).fetchone()[0]
        self.assertEqual(count, 1)


# ===========================================================================
# TestClaimPermutationConcurrent  (file-based DB, two threads racing)
# ===========================================================================

class TestClaimPermutationConcurrent(unittest.TestCase):

    def setUp(self):
        self._tmp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self._tmp_dir.name, 'test.db')
        # Initialise schema before threads start.
        conn = _make_connection(self.db_path)
        conn.close()

    def tearDown(self):
        self._tmp_dir.cleanup()

    def _race(self, perm_a: list, perm_b: list) -> tuple:
        """Launch two threads, each claiming one perm. Return (results, errors)."""
        results = []
        errors = []
        barrier = threading.Barrier(2)

        def worker(perm):
            try:
                conn = _make_connection(self.db_path)
                rkey = make_rotation_key(perm)
                barrier.wait()  # Synchronise to maximise race window.
                result = claim_permutation(conn, perm, rkey)
                results.append(result)
                conn.close()
            except Exception as exc:
                errors.append(exc)

        t1 = threading.Thread(target=worker, args=(perm_a,))
        t2 = threading.Thread(target=worker, args=(perm_b,))
        t1.start()
        t2.start()
        t1.join(timeout=60)
        t2.join(timeout=60)
        return results, errors

    def test_same_perm_exactly_one_succeeds(self):
        """Two threads racing to claim identical permutations: one wins, one loses."""
        p = _seeded_perm(42)
        results, errors = self._race(p, p)

        self.assertFalse(errors, f"Worker exceptions: {errors}")
        self.assertEqual(len(results), 2)
        self.assertEqual(len([r for r in results if r is not None]), 1)
        self.assertEqual(len([r for r in results if r is None]), 1)

    def test_rotation_exactly_one_succeeds(self):
        """Thread A claims P; thread B claims rotation(P, 1). One must win."""
        p = _seeded_perm(42)
        results, errors = self._race(p, _rotate(p, 1))

        self.assertFalse(errors, f"Worker exceptions: {errors}")
        self.assertEqual(len(results), 2)
        self.assertEqual(len([r for r in results if r is not None]), 1)
        self.assertEqual(len([r for r in results if r is None]), 1)

    def test_reverse_exactly_one_succeeds(self):
        """Thread A claims P; thread B claims reverse(P). One must win."""
        p = _seeded_perm(42)
        results, errors = self._race(p, _reverse(p))

        self.assertFalse(errors, f"Worker exceptions: {errors}")
        self.assertEqual(len(results), 2)
        self.assertEqual(len([r for r in results if r is not None]), 1)
        self.assertEqual(len([r for r in results if r is None]), 1)

    def test_concurrent_db_row_count_is_one(self):
        """After the race, the database must contain exactly one row."""
        p = _seeded_perm(42)
        self._race(p, _rotate(p, 32))

        conn = _make_connection(self.db_path)
        count = conn.execute(
            'SELECT COUNT(*) FROM rotor_configurations'
        ).fetchone()[0]
        conn.close()
        self.assertEqual(count, 1)


# ===========================================================================
# TestUpdateScores
# ===========================================================================

class TestUpdateScores(unittest.TestCase):

    def setUp(self):
        self.conn = _make_connection()

    def tearDown(self):
        self.conn.close()

    def _claim_and_score(self, seed: int = 42):
        p = _seeded_perm(seed)
        row_id = claim_permutation(self.conn, p, make_rotation_key(p))
        scores = compute_score(p)
        return row_id, scores

    def test_score_total_null_before_update(self):
        row_id, scores = self._claim_and_score()
        result = self.conn.execute(
            'SELECT score_total FROM rotor_configurations WHERE id = ?', (row_id,)
        ).fetchone()[0]
        self.assertIsNone(result)

    def test_all_scores_written_correctly(self):
        row_id, scores = self._claim_and_score()
        update_scores(self.conn, row_id, scores)

        row = self.conn.execute(
            'SELECT score_total, score_c1_displacement, score_c2_fixed_points, '
            'fixed_point_count, score_c3_cycles, score_c4_runs, score_c5_uniformity '
            'FROM rotor_configurations WHERE id = ?',
            (row_id,)
        ).fetchone()

        self.assertAlmostEqual(row[0], scores['score_total'],           places=4)
        self.assertAlmostEqual(row[1], scores['score_c1_displacement'], places=4)
        self.assertAlmostEqual(row[2], scores['score_c2_fixed_points'], places=4)
        self.assertEqual(      row[3], scores['fixed_point_count'])
        self.assertAlmostEqual(row[4], scores['score_c3_cycles'],       places=4)
        self.assertAlmostEqual(row[5], scores['score_c4_runs'],         places=4)
        self.assertAlmostEqual(row[6], scores['score_c5_uniformity'],   places=4)

    def test_score_total_non_null_after_update(self):
        row_id, scores = self._claim_and_score()
        update_scores(self.conn, row_id, scores)
        result = self.conn.execute(
            'SELECT score_total FROM rotor_configurations WHERE id = ?', (row_id,)
        ).fetchone()[0]
        self.assertIsNotNone(result)

    def test_update_overwrites_previous_values(self):
        row_id, scores = self._claim_and_score()
        update_scores(self.conn, row_id, scores)
        modified = {k: (v / 2.0 if k != 'fixed_point_count' else 0)
                    for k, v in scores.items()}
        update_scores(self.conn, row_id, modified)
        result = self.conn.execute(
            'SELECT score_total FROM rotor_configurations WHERE id = ?', (row_id,)
        ).fetchone()[0]
        self.assertAlmostEqual(result, modified['score_total'], places=4)


# ===========================================================================
# TestComputeScore
# ===========================================================================

class TestComputeScore(unittest.TestCase):

    def test_identity_all_components_zero(self):
        """Identity: zero displacement, all fixed points -> every component = 0."""
        s = compute_score(list(range(N)))
        self.assertAlmostEqual(s['score_c1_displacement'], 0.0)
        self.assertAlmostEqual(s['score_c2_fixed_points'], 0.0)
        self.assertAlmostEqual(s['score_c5_uniformity'],   0.0)
        self.assertEqual(s['fixed_point_count'], N)
        self.assertAlmostEqual(s['score_total'], 0.0)

    def test_shift32_known_values(self):
        """Shift-by-32: maximum ring displacement, no fixed points.

        Expected values derived analytically:
          C1 = 30 * (32 / 32) = 30.0
          C2 = 20 * (64 / 64) = 20.0
          C3 = 5*(1 - 32/32) + 5*(2/32) = 0.3125  (32 cycles of length 2)
          C4 = 0.0  (max consecutive run = 32, clamped)
          C5 = 20 * (32 / 32) = 20.0
          total = 70.3125
        """
        p = [(i + 32) % N for i in range(N)]
        s = compute_score(p)
        self.assertAlmostEqual(s['score_c1_displacement'], 30.0,    places=4)
        self.assertAlmostEqual(s['score_c2_fixed_points'], 20.0,    places=4)
        self.assertAlmostEqual(s['score_c3_cycles'],        0.3125, places=4)
        self.assertAlmostEqual(s['score_c4_runs'],          0.0,    places=4)
        self.assertAlmostEqual(s['score_c5_uniformity'],   20.0,    places=4)
        self.assertAlmostEqual(s['score_total'],           70.3125, places=4)
        self.assertEqual(s['fixed_point_count'], 0)

    def test_pair_swap_known_c1_and_c2(self):
        """[1,0,3,2,...]: displacement=1 for every position, no fixed points.

          C1 = 30 * (1 / 32) = 0.9375
          C2 = 20 * (64 / 64) = 20.0
        """
        s = compute_score(_pair_swap_perm())
        self.assertAlmostEqual(s['score_c1_displacement'], 0.9375, places=4)
        self.assertAlmostEqual(s['score_c2_fixed_points'], 20.0,   places=4)
        self.assertEqual(s['fixed_point_count'], 0)

    def test_score_total_in_bounds(self):
        """Total score must always lie in [0, 100] for any permutation."""
        import random
        rng = random.Random(12345)
        for _ in range(50):
            p = list(range(N))
            rng.shuffle(p)
            s = compute_score(p)
            self.assertGreaterEqual(s['score_total'], 0.0)
            self.assertLessEqual(s['score_total'], 100.0)

    def test_all_components_non_negative(self):
        """No individual component should fall below zero."""
        import random
        rng = random.Random(99)
        keys = (
            'score_c1_displacement', 'score_c2_fixed_points',
            'score_c3_cycles', 'score_c4_runs', 'score_c5_uniformity',
        )
        for _ in range(30):
            p = list(range(N))
            rng.shuffle(p)
            s = compute_score(p)
            for k in keys:
                with self.subTest(component=k):
                    self.assertGreaterEqual(s[k], 0.0)

    def test_fixed_point_count_matches_manual_count(self):
        import random
        rng = random.Random(7)
        for _ in range(20):
            p = list(range(N))
            rng.shuffle(p)
            expected = sum(1 for i in range(N) if p[i] == i)
            self.assertEqual(compute_score(p)['fixed_point_count'], expected)

    def test_c2_zero_when_all_fixed(self):
        s = compute_score(list(range(N)))
        self.assertAlmostEqual(s['score_c2_fixed_points'], 0.0)

    def test_c2_max_when_no_fixed_points(self):
        # Cyclic shift by 1: p[i] = (i+1)%N, guaranteed no fixed points.
        p = [(i + 1) % N for i in range(N)]
        s = compute_score(p)
        self.assertEqual(s['fixed_point_count'], 0)
        self.assertAlmostEqual(s['score_c2_fixed_points'], 20.0)


# ===========================================================================
# TestRunSeededBatch
# ===========================================================================

class TestRunSeededBatch(unittest.TestCase):

    def setUp(self):
        self.conn = _make_connection()

    def tearDown(self):
        self.conn.close()

    def _identity_generate(self, seed: int) -> list:
        """Always returns the identity — used to verify fixed-seed processing."""
        return list(range(N))

    def _seeded_generate(self, seed: int) -> list:
        return _seeded_perm(seed)

    def test_returns_correct_next_seed(self):
        ins, skp, next_seed = run_seeded_batch(self._seeded_generate, 0, 5, self.conn)
        self.assertEqual(next_seed, 5)

    def test_processes_exactly_seed_count_seeds(self):
        """inserted + skipped must always equal seed_count."""
        for seed_count in [1, 5, 10]:
            with self.subTest(seed_count=seed_count):
                conn = _make_connection()
                ins, skp, _ = run_seeded_batch(self._seeded_generate, 0, seed_count, conn)
                self.assertEqual(ins + skp, seed_count)
                conn.close()

    def test_new_perms_are_inserted(self):
        ins, skp, _ = run_seeded_batch(self._seeded_generate, 0, 10, self.conn)
        self.assertGreater(ins, 0)
        count = self.conn.execute(
            'SELECT COUNT(*) FROM rotor_configurations'
        ).fetchone()[0]
        self.assertEqual(count, ins)

    def test_inserted_rows_have_scores(self):
        """Every row inserted by run_seeded_batch must have non-NULL score_total."""
        run_seeded_batch(self._seeded_generate, 0, 5, self.conn)
        null_scores = self.conn.execute(
            'SELECT COUNT(*) FROM rotor_configurations WHERE score_total IS NULL'
        ).fetchone()[0]
        self.assertEqual(null_scores, 0)

    def test_duplicates_are_skipped(self):
        """Running the same seeds twice: second run should insert=0, skipped=N."""
        run_seeded_batch(self._seeded_generate, 0, 5, self.conn)
        ins, skp, _ = run_seeded_batch(self._seeded_generate, 0, 5, self.conn)
        self.assertEqual(ins, 0)
        self.assertEqual(skp, 5)

    def test_row_count_unchanged_on_all_duplicates(self):
        run_seeded_batch(self._seeded_generate, 0, 5, self.conn)
        count_before = self.conn.execute(
            'SELECT COUNT(*) FROM rotor_configurations'
        ).fetchone()[0]
        run_seeded_batch(self._seeded_generate, 0, 5, self.conn)
        count_after = self.conn.execute(
            'SELECT COUNT(*) FROM rotor_configurations'
        ).fetchone()[0]
        self.assertEqual(count_before, count_after)

    def test_partial_duplicate_batch(self):
        """Seeds 0-4 inserted first; seeds 0-9 run next: 5 inserted, 5 skipped."""
        run_seeded_batch(self._seeded_generate, 0, 5, self.conn)
        ins, skp, _ = run_seeded_batch(self._seeded_generate, 0, 10, self.conn)
        self.assertEqual(skp, 5)
        self.assertEqual(ins, 5)



# ===========================================================================
# TestWorkerE
# ===========================================================================

class TestWorkerE(unittest.TestCase):
    """Tests for worker_e.generate() — a pure function, no DB required."""

    def test_output_is_valid_permutation(self):
        """generate() must return a permutation of 0..N-1."""
        for seed in range(20):
            with self.subTest(seed=seed):
                p = worker_e.generate(seed)
                self.assertEqual(sorted(p), list(range(N)))

    def test_output_length(self):
        self.assertEqual(len(worker_e.generate(0)), N)

    def test_score_in_target_band(self):
        """100% of Worker E output should land in the 30-49 score band."""
        for seed in range(50):
            with self.subTest(seed=seed):
                p = worker_e.generate(seed)
                s = compute_score(p)['score_total']
                self.assertGreaterEqual(s, 30.0, f"seed={seed} score={s:.2f} below 30")
                self.assertLess(s, 50.0,         f"seed={seed} score={s:.2f} above 49.99")

    def test_not_all_same_output(self):
        """Different seeds must not always produce the same permutation."""
        perms = [tuple(worker_e.generate(s)) for s in range(10)]
        self.assertGreater(len(set(perms)), 1)

    def test_deterministic(self):
        """Same seed must always produce the same permutation."""
        self.assertEqual(worker_e.generate(42), worker_e.generate(42))



# ===========================================================================
# TestWorkerF
# ===========================================================================

class TestWorkerF(unittest.TestCase):
    """Tests for worker_f.generate() — partial Fisher-Yates, targets 20-29."""

    def test_output_is_valid_permutation(self):
        for seed in range(20):
            with self.subTest(seed=seed):
                self.assertEqual(sorted(worker_f.generate(seed)), list(range(N)))

    def test_output_length(self):
        self.assertEqual(len(worker_f.generate(0)), N)

    def test_deterministic(self):
        self.assertEqual(worker_f.generate(42), worker_f.generate(42))

    def test_not_all_same_output(self):
        perms = [tuple(worker_f.generate(s)) for s in range(10)]
        self.assertGreater(len(set(perms)), 1)

    def test_majority_in_target_band(self):
        """At least 60% of Worker F output must land in the 20-29 score band."""
        hits = sum(
            1 for s in range(200)
            if 20.0 <= compute_score(worker_f.generate(s))['score_total'] < 30.0
        )
        self.assertGreaterEqual(hits / 200, 0.60,
                                f"Only {hits}/200 seeds landed in 20-29")

    def test_has_fixed_points(self):
        """Partial shuffle must leave some positions fixed (34 out of 64 are untouched)."""
        fp = compute_score(worker_f.generate(0))['fixed_point_count']
        self.assertGreater(fp, 0)


# ===========================================================================
# TestWorkerG
# ===========================================================================

class TestWorkerG(unittest.TestCase):
    """Tests for worker_g.generate() — adjacent pair swaps on shift-by-32, targets 80-89."""

    def test_output_is_valid_permutation(self):
        for seed in range(20):
            with self.subTest(seed=seed):
                self.assertEqual(sorted(worker_g.generate(seed)), list(range(N)))

    def test_output_length(self):
        self.assertEqual(len(worker_g.generate(0)), N)

    def test_deterministic(self):
        self.assertEqual(worker_g.generate(42), worker_g.generate(42))

    def test_not_all_same_output(self):
        perms = [tuple(worker_g.generate(s)) for s in range(10)]
        self.assertGreater(len(set(perms)), 1)

    def test_all_in_target_band(self):
        """100% of Worker G output must land in the 80-89 score band."""
        for seed in range(100):
            with self.subTest(seed=seed):
                s = compute_score(worker_g.generate(seed))['score_total']
                self.assertGreaterEqual(s, 80.0, f"seed={seed} score={s:.2f} below 80")
                self.assertLess(s, 90.0,         f"seed={seed} score={s:.2f} above 89.99")

    def test_no_fixed_points(self):
        """Shift-by-32 base ensures no fixed points regardless of pair swaps."""
        for seed in range(20):
            with self.subTest(seed=seed):
                fp = compute_score(worker_g.generate(seed))['fixed_point_count']
                self.assertEqual(fp, 0)


# ===========================================================================
# TestOrchestrator
# ===========================================================================

class TestOrchestrator(unittest.TestCase):
    """Smoke tests for orchestrator.main() using a temp DB.

    The conn_factory parameter redirects all DB access to an isolated temp
    file so the production database is never touched.
    """

    def setUp(self):
        self._tmpdir = tempfile.TemporaryDirectory()
        db_path = os.path.join(self._tmpdir.name, 'test.db')
        self._db_path = db_path

        def _factory():
            conn = sqlite3.connect(db_path, timeout=30, check_same_thread=False)
            conn.isolation_level = None
            conn.execute(_CREATE_TABLE)
            conn.execute(_CREATE_INDEX)
            return conn

        self._factory = _factory

    def tearDown(self):
        self._tmpdir.cleanup()

    def test_single_round_inserts_rows(self):
        """One round with Worker E should insert rows into the temp DB."""
        orchestrator.main(
            ['E'],
            seed_overrides={'E': 4_000_000},
            max_rounds=1,
            conn_factory=self._factory,
        )
        conn = self._factory()
        count = conn.execute(
            'SELECT COUNT(*) FROM rotor_configurations'
        ).fetchone()[0]
        conn.close()
        self.assertGreater(count, 0)

    def test_state_table_created_after_run(self):
        """worker_state table must exist and contain the active worker after one round."""
        orchestrator.main(
            ['E'],
            seed_overrides={'E': 4_000_000},
            max_rounds=1,
            conn_factory=self._factory,
        )
        conn = self._factory()
        rows = conn.execute(
            "SELECT worker_id FROM worker_state WHERE worker_id = 'E'"
        ).fetchall()
        conn.close()
        self.assertEqual(len(rows), 1)

    def test_seed_advances_after_round(self):
        """Saved seed must be greater than the start seed after one round."""
        start_seed = 4_000_000
        orchestrator.main(
            ['E'],
            seed_overrides={'E': start_seed},
            max_rounds=1,
            conn_factory=self._factory,
        )
        conn = self._factory()
        saved_seed = conn.execute(
            "SELECT current_seed FROM worker_state WHERE worker_id = 'E'"
        ).fetchone()[0]
        conn.close()
        self.assertGreater(saved_seed, start_seed)

    def test_multiple_workers_in_parallel(self):
        """Two worker slots must both populate the state table."""
        orchestrator.main(
            ['E', 'E2'],
            seed_overrides={'E': 4_000_000, 'E2': 5_000_000},
            max_rounds=1,
            conn_factory=self._factory,
        )
        conn = self._factory()
        rows = conn.execute(
            "SELECT worker_id FROM worker_state ORDER BY worker_id"
        ).fetchall()
        conn.close()
        worker_ids = [r[0] for r in rows]
        self.assertIn('E',  worker_ids)
        self.assertIn('E2', worker_ids)

    def test_unknown_worker_id_exits(self):
        """An unrecognised worker ID must raise SystemExit."""
        with self.assertRaises(SystemExit):
            orchestrator.main(
                ['UNKNOWN'],
                conn_factory=self._factory,
            )

    def test_inserted_rows_have_non_null_scores(self):
        """Every row written during a smoke run must have a computed score."""
        orchestrator.main(
            ['E'],
            seed_overrides={'E': 4_000_000},
            max_rounds=1,
            conn_factory=self._factory,
        )
        conn = self._factory()
        null_count = conn.execute(
            'SELECT COUNT(*) FROM rotor_configurations WHERE score_total IS NULL'
        ).fetchone()[0]
        conn.close()
        self.assertEqual(null_count, 0)

    def test_consecutive_fails_increments_on_all_duplicate_batch(self):
        """consecutive_fails in worker_state must increment when every seed is a duplicate."""
        # Pre-insert the identity permutation so all seeds from a generator that
        # always returns identity will be duplicates.
        p = list(range(N))
        conn = self._factory()
        row_id = claim_permutation(conn, p, make_rotation_key(p))
        update_scores(conn, row_id, compute_score(p))
        conn.close()

        def _always_identity(seed):
            return list(range(N))

        orig_registry = {k: dict(v) for k, v in orchestrator._WORKER_REGISTRY.items()}
        orchestrator._WORKER_REGISTRY['E'] = {
            'generate': _always_identity,
            'default_seed': 4_000_000,
        }
        try:
            orchestrator.main(
                ['E'],
                seed_overrides={'E': 4_000_000},
                max_rounds=1,
                conn_factory=self._factory,
            )
        finally:
            orchestrator._WORKER_REGISTRY.clear()
            orchestrator._WORKER_REGISTRY.update(orig_registry)

        conn = self._factory()
        cf = conn.execute(
            "SELECT consecutive_fails FROM worker_state WHERE worker_id = 'E'"
        ).fetchone()[0]
        conn.close()
        self.assertGreater(cf, 0)

    def test_all_workers_done_terminates(self):
        """Orchestrator must stop when all workers hit FAIL_THRESHOLD consecutive all-dup batches."""
        p = list(range(N))
        conn = self._factory()
        row_id = claim_permutation(conn, p, make_rotation_key(p))
        update_scores(conn, row_id, compute_score(p))
        conn.close()

        def _always_identity(seed):
            return list(range(N))

        orig_registry = {k: dict(v) for k, v in orchestrator._WORKER_REGISTRY.items()}
        orig_threshold = orchestrator.FAIL_THRESHOLD
        orchestrator._WORKER_REGISTRY['E'] = {
            'generate': _always_identity,
            'default_seed': 4_000_000,
        }
        orchestrator.FAIL_THRESHOLD = 1
        try:
            # No max_rounds — must self-terminate via the all-done path
            orchestrator.main(
                ['E'],
                seed_overrides={'E': 4_000_000},
                conn_factory=self._factory,
            )
        finally:
            orchestrator.FAIL_THRESHOLD = orig_threshold
            orchestrator._WORKER_REGISTRY.clear()
            orchestrator._WORKER_REGISTRY.update(orig_registry)

        conn = self._factory()
        is_done = conn.execute(
            "SELECT is_done FROM worker_state WHERE worker_id = 'E'"
        ).fetchone()[0]
        conn.close()
        self.assertEqual(is_done, 1)

    def test_newly_done_message_printed_when_other_workers_remain(self):
        """The 'waiting for' message must print when one worker finishes but others are still running."""
        # Pre-insert identity so E's generator (always identity) produces only duplicates.
        p = list(range(N))
        conn = self._factory()
        row_id = claim_permutation(conn, p, make_rotation_key(p))
        update_scores(conn, row_id, compute_score(p))
        conn.close()

        def _always_identity(seed):
            return list(range(N))

        orig_registry = {k: dict(v) for k, v in orchestrator._WORKER_REGISTRY.items()}
        orig_threshold = orchestrator.FAIL_THRESHOLD
        # E always duplicates → done after 1 batch; E2 uses fresh seeds → still running.
        orchestrator._WORKER_REGISTRY['E'] = {
            'generate': _always_identity,
            'default_seed': 4_000_000,
        }
        orchestrator.FAIL_THRESHOLD = 1
        try:
            # max_rounds=1: E becomes done, E2 still running → "waiting for" message fires
            orchestrator.main(
                ['E', 'E2'],
                seed_overrides={'E': 4_000_000, 'E2': 5_000_000},
                max_rounds=1,
                conn_factory=self._factory,
            )
        finally:
            orchestrator.FAIL_THRESHOLD = orig_threshold
            orchestrator._WORKER_REGISTRY.clear()
            orchestrator._WORKER_REGISTRY.update(orig_registry)

        conn = self._factory()
        e_done  = conn.execute("SELECT is_done FROM worker_state WHERE worker_id='E'").fetchone()[0]
        e2_done = conn.execute("SELECT is_done FROM worker_state WHERE worker_id='E2'").fetchone()[0]
        conn.close()
        self.assertEqual(e_done, 1,  "E should be marked done")
        self.assertEqual(e2_done, 0, "E2 should still be running")

    def test_db_size_limit_terminates(self):
        """Orchestrator must stop immediately when the DB exceeds MAX_DB_BYTES."""
        orig = orchestrator.MAX_DB_BYTES
        orchestrator.MAX_DB_BYTES = 0  # Any real DB file will exceed 0 bytes
        try:
            orchestrator.main(
                ['E'],
                seed_overrides={'E': 4_000_000},
                conn_factory=self._factory,
            )
        finally:
            orchestrator.MAX_DB_BYTES = orig

        # No rows should have been inserted — the size check fires before the batch
        conn = self._factory()
        count = conn.execute(
            'SELECT COUNT(*) FROM rotor_configurations'
        ).fetchone()[0]
        conn.close()
        self.assertEqual(count, 0)


# ---------------------------------------------------------------------------
# Worker H tests
# ---------------------------------------------------------------------------

class TestWorkerH(unittest.TestCase):
    """Tests for worker_h generate() function and score-band distribution."""

    def test_returns_list_of_correct_length(self):
        perm = worker_h.generate(10_000_000)
        self.assertEqual(len(perm), N)

    def test_is_valid_permutation(self):
        perm = worker_h.generate(10_000_001)
        self.assertEqual(sorted(perm), list(range(N)))

    def test_different_seeds_produce_different_outputs(self):
        p1 = worker_h.generate(10_000_000)
        p2 = worker_h.generate(10_000_001)
        self.assertNotEqual(p1, p2)

    def test_same_seed_produces_same_output(self):
        p1 = worker_h.generate(10_000_000)
        p2 = worker_h.generate(10_000_000)
        self.assertEqual(p1, p2)

    def test_score_band_distribution_mostly_80_89(self):
        """At least 90% of outputs should land in the 80-89 score band."""
        in_band = 0
        trials = 200
        for seed in range(10_000_000, 10_000_000 + trials):
            perm = worker_h.generate(seed)
            scores = compute_score(perm)
            total = scores['score_total']
            if 80 <= total < 90:
                in_band += 1
        hit_rate = in_band / trials
        self.assertGreaterEqual(
            hit_rate, 0.90,
            f"Expected >=90% in 80-89 band, got {hit_rate:.1%} ({in_band}/{trials})",
        )

    def test_fixed_points_are_rare(self):
        """Worker H is not a strict derangement generator, but fixed points should be rare."""
        total_fixed = 0
        seeds_tested = 20
        for seed in range(10_000_000, 10_000_000 + seeds_tested):
            perm = worker_h.generate(seed)
            total_fixed += sum(1 for i in range(N) if perm[i] == i)
        fixed_rate = total_fixed / (seeds_tested * N)
        self.assertLess(
            fixed_rate, 0.10,
            f"Fixed-point rate {fixed_rate:.1%} is too high for a high-complexity worker",
        )

    def test_mean_ring_distance_is_high(self):
        """Mean ring distance should be well above 16 (random baseline)."""
        for seed in range(10_000_000, 10_000_010):
            with self.subTest(seed=seed):
                perm = worker_h.generate(seed)
                mean_dist = sum(ring_dist(perm[i], i) for i in range(N)) / N
                self.assertGreater(
                    mean_dist, 20.0,
                    f"Seed {seed} mean ring distance {mean_dist:.2f} too low",
                )

    def test_registered_in_orchestrator(self):
        """Orchestrator must have H, H2, H3, H4 slots with correct seed offsets."""
        for slot, expected_seed in [
            ('H',  10_000_000),
            ('H2', 11_000_000),
            ('H3', 12_000_000),
            ('H4', 13_000_000),
        ]:
            with self.subTest(slot=slot):
                self.assertIn(slot, orchestrator._WORKER_REGISTRY)
                self.assertEqual(
                    orchestrator._WORKER_REGISTRY[slot]['default_seed'],
                    expected_seed,
                )


if __name__ == '__main__':
    unittest.main(verbosity=2)
