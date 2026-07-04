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
