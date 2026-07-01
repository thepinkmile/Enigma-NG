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
