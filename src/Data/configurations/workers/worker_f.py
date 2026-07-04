"""Worker F: low-mid range, targeting score band 20-29.

Generates permutations using a partial Fisher-Yates shuffle: exactly 30 of the
64 positions are chosen at random and shuffled among themselves, while the
remaining 34 positions stay fixed. This produces a mix of moderate displacement
and many fixed points, which reliably lands in the 20-29 score band (~80% hit
rate; the remaining ~20% fall into the adjacent 10-19 band).

Seed namespace: 8,000,000+

Usage: python worker_f.py [seed_start=8000000] [batch_size=100]
"""

import random
import sys

from worker_utils import (N, claim_permutation, compute_score, get_connection,
                           make_rotation_key, update_scores)

_SHUFFLE_K = 30  # positions to shuffle out of N


def generate(seed: int) -> list:
    rng = random.Random(seed)
    perm = list(range(N))
    positions = rng.sample(range(N), _SHUFFLE_K)
    subset = [perm[p] for p in positions]
    rng.shuffle(subset)
    for p, v in zip(positions, subset):
        perm[p] = v
    return perm


def run_batch(seed_start: int = 8_000_000, batch_size: int = 100) -> int:  # pragma: no cover
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
            print(f'[F] {inserted:>3}/{batch_size}  id={row_id:<6}  '
                  f'score={scores["score_total"]:6.2f}  seed={seed - 1}')
        else:
            skipped += 1
    conn.close()
    print(f'[F] Done. inserted={inserted}  skipped={skipped}  next_seed={seed}')
    return seed


if __name__ == '__main__':  # pragma: no cover
    s = int(sys.argv[1]) if len(sys.argv) > 1 else 8_000_000
    b = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    run_batch(s, b)
