"""Worker E: mid-range complexity, targeting score band 30-49.

Generates permutations using a 'stride-swap' base: positions are swapped in
pairs at distance d (d randomly chosen from {1, 2, 4, 8}), followed by a
small number of random transpositions for variety. This reliably produces
permutations in the 30-49 score band, filling the gap left by the other
workers whose strategies naturally cluster in the 0-25 and 50-85 ranges.

Usage: python worker_e.py [seed_start=4000000] [batch_size=100]
"""

import random
import sys

from worker_utils import (N, claim_permutation, compute_score, get_connection,
                           make_rotation_key, update_scores)

_STRIDES = [1, 2, 4, 8]


def generate(seed: int) -> list:
    rng = random.Random(seed)
    d = rng.choice(_STRIDES)
    perm = list(range(N))
    for start in range(0, N, 2 * d):
        for i in range(start, start + d):
            perm[i], perm[i + d] = perm[i + d], perm[i]
    for _ in range(rng.randint(0, 6)):
        i, j = rng.sample(range(N), 2)
        perm[i], perm[j] = perm[j], perm[i]
    return perm


def run_batch(seed_start: int = 4_000_000, batch_size: int = 100) -> int:  # pragma: no cover
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
            print(f'[E] {inserted:>3}/{batch_size}  id={row_id:<6}  '
                  f'score={scores["score_total"]:6.2f}  seed={seed - 1}')
        else:
            skipped += 1
    conn.close()
    print(f'[E] Done. inserted={inserted}  skipped={skipped}  next_seed={seed}')
    return seed


if __name__ == '__main__':  # pragma: no cover
    s = int(sys.argv[1]) if len(sys.argv) > 1 else 4_000_000
    b = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    run_batch(s, b)
