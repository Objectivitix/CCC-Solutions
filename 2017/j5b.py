# O(N + L_i^2) solution.
# Gets 15/15 points.
# Had to write some uglier code in `two_sum` to shave
# off some constant factors. (Python moment :weary:)

from collections import defaultdict, Counter


def two_sum(s, counter):
    complements = {}

    for n, count in counter.items():
        if s % 2 == 0 and n == s // 2:
            yield count // 2
            continue

        a = complements.get(s - n, 0)
        if a < count:
            valid = a
        else:
            valid = count

        if valid > 0:
            complements[s - n] -= valid
            yield valid
            continue

        complements[n] = count


_ = input()
COUNTER = Counter(map(int, input().split()))

possible_dimensions = defaultdict(list)

for height in range(2, 4001):
    length = sum(two_sum(height, COUNTER))
    possible_dimensions[length].append(height)

max_length = max(possible_dimensions)
heights_n = len(possible_dimensions[max_length])

print(max_length, heights_n)
