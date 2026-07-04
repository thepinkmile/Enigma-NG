"""Worker G: high-complexity, targeting score band 80-89.

Generates permutations using a modified shift-by-32 base: the shift-by-32
permutation (maximum ring displacement) has all its 32 non-overlapping
adjacent pairs (positions 0-1, 2-3, 4-5, ..., 62-63) randomly selected for
swapping, with between 30 and 32 pairs swapped per permutation.

This combination reliably produces 100% of output in the 80-89 band because:
  - C1 stays near 29 (ring distance drops from 32 to 31 per swapped pair)
  - C2 = 20 (no fixed points)
  - C4 = 17.5 (adjacent pair swaps cap max_run at 2, since swapped pairs form
    descending pairs that break all ascending runs)
  - C5 stays near 19.4 (all ring distances are 31)

Swapping 30-32 pairs out of 32 ensures at most two consecutive unswapped pairs,
keeping max_run <= 4 and C4 >= 12.5, which keeps the total firmly in 80-89.

Seed namespace: 9,000,000+

Usage: python worker_g.py [seed_start=9000000] [batch_size=100]
"""

import random
import sys

from worker_utils import (N, claim_permutation, compute_score, get_connection,
                           make_rotation_key, update_scores)

_BASE = [(i + N // 2) % N for i in range(N)]  # shift-by-32
_PAIR_STARTS = list(range(0, N, 2))            # [0, 2, 4, ..., 62]


def generate(seed: int) -> list:
    rng = random.Random(seed)
    perm = _BASE[:]
    pair_order = _PAIR_STARTS[:]
    rng.shuffle(pair_order)
    n_swaps = rng.randint(30, 32)
    for i in pair_order[:n_swaps]:
        perm[i], perm[i + 1] = perm[i + 1], perm[i]
    return perm


def run_batch(seed_start: int = 9_000_000, batch_size: int = 100) -> int:  # pragma: no cover
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
            print(f'[G] {inserted:>3}/{batch_size}  id={row_id:<6}  '
                  f'score={scores["score_total"]:6.2f}  seed={seed - 1}')
        else:
            skipped += 1
    conn.close()
    print(f'[G] Done. inserted={inserted}  skipped={skipped}  next_seed={seed}')
    return seed


if __name__ == '__main__':  # pragma: no cover
    s = int(sys.argv[1]) if len(sys.argv) > 1 else 9_000_000
    b = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    run_batch(s, b)
