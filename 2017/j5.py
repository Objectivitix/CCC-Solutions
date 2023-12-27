from collections import defaultdict

_ = input()
arr = list(map(int, input().split()))

sums_to_pairs = defaultdict(list)

for i, value in enumerate(arr):
    for j, other in enumerate(arr[i + 1:], start=i + 1):
        sums_to_pairs[value + other].append((i, j))

sums_to_pair_numbers = {}

for s, pairs in sums_to_pairs.items():
    pairs_n = 0
    indices_used = set()

    for pair in pairs:
        if pair[0] in indices_used or pair[1] in indices_used:
            continue

        pairs_n += 1
        indices_used.add(pair[0])
        indices_used.add(pair[1])

    sums_to_pair_numbers[s] = pairs_n

sums_to_pair_numbers_sorted = sorted(
    sums_to_pair_numbers.items(),
    key=lambda kv: kv[1],
    reverse=True,
)

it = iter(sums_to_pair_numbers_sorted)
_, first = next(it)

same_sums_n = 1

for _, pairs_n in it:
    if pairs_n == first:
        same_sums_n += 1
    else:
        break

print(first, same_sums_n)
