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
