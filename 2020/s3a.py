# O(|H|*|N|) solution - both time and space.
# Gets 7/15 points.

from collections import Counter

NEEDLE = Counter(input())
N = sum(NEEDLE.values())

HAYSTACK = input()

distinct_permutations = set()

for char_list in zip(*(HAYSTACK[i:] for i in range(N))):
    if Counter(char_list) == NEEDLE:
        distinct_permutations.add("".join(char_list))

print(len(distinct_permutations))
