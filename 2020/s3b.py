# O(|H| + |N|) by sliding window and rolling hash.
# We can make further constant optimizations. But
# it gets full points, so who cares :P

from collections import Counter
from string import ascii_lowercase

BASE = 26
MODULUS = 2 ** 107 - 1  # fingers crossed no collisions


def hash_(string):
    num = 0

    for char in string:
        num += ord(char)
        num *= BASE
        num %= MODULUS

    return num


NEEDLE = Counter(input())
N = sum(NEEDLE.values())

HAYSTACK = input()

distinct_permutations = set()

counter = Counter(HAYSTACK[:N])
substring_hash = hash_(HAYSTACK[:N])

sliding = zip(HAYSTACK, HAYSTACK[N:])

while True:
    if all(
        counter[letter] == NEEDLE[letter]
        for letter in ascii_lowercase
    ):
        distinct_permutations.add(substring_hash)

    window = next(sliding, None)

    if not window:
        break

    deleted, added = window

    counter[deleted] -= 1
    counter[added] += 1

    substring_hash -= ord(deleted) * pow(BASE, N, MODULUS)
    substring_hash += ord(added)
    substring_hash *= BASE
    substring_hash %= MODULUS

print(len(distinct_permutations))
