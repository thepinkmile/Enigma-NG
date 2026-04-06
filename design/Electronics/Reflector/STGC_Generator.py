def find_stgc(num_positions, num_sensors):
    def get_word(track, pos):
        # Extract n bits starting from 'pos', wrapping around the track
        word = 0
        for i in range(num_sensors):
            bit = track[(pos + i) % len(track)]
            word |= (bit << i)
        return word

    def is_gray(w1, w2):
        # Check if exactly one bit changed
        diff = w1 ^ w2
        return diff != 0 and (diff & (diff - 1)) == 0

    def backtrack(track, used_words):
        if len(track) == num_positions:
            # Check cyclic Gray property (last word vs first word)
            if is_gray(get_word(track, num_positions - 1), get_word(track, 0)):
                return track
            return None

        # Try appending 1 or 0
        for bit in [1, 0]:
            track.append(bit)
            current_pos = len(track) - num_sensors

            if current_pos >= 0:
                new_word = get_word(track, current_pos)
                prev_word = get_word(track, current_pos - 1)

                if new_word not in used_words and is_gray(prev_word, new_word):
                    used_words.add(new_word)
                    if backtrack(track, used_words): return track
                    used_words.remove(new_word)
            else:
                # Still building initial 'seed' bits
                if backtrack(track, used_words): return track

            track.pop()
        return None

    # Start with a string of zeros equal to sensor count
    start_track = [0] * num_sensors
    return backtrack(start_track, {0})

# Example Usage:
pattern_26 = find_stgc(26, 5)
print(f"26-Pos Track: {''.join(map(str, pattern_26))}")
