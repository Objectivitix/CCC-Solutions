# https://dmoj.ca/problem/ccc16s4/editorial
#
# WOW. This problem was AMAZING. DP + PSA + two pointers?!
# LOVED IT. Also TIL that using your own memo dict performs
# better than `functools.lru_cache`, even `functools.cache`.

from itertools import accumulate


def query_sum(l, r):
    return CUM[r] - (CUM[l - 1] if l > 0 else 0)


def get_valid_splits(i, j):
    complements = {}

    for p in range(i, j + 1):
        complements[query_sum(i, p)] = p

        q = complements.get(query_sum(p, j))
        if q is not None:
            yield q, p


def can_combine(i, j):
    # BASE CASE: if one riceball (==)
    # or auto passing the middle condition
    # when combining two (a + 1 > b - 1)
    if i >= j:
        return True

    if (i, j) in memo:
        return memo[i, j]

    memo[i, j] = any(
        can_combine(i, a)
        and can_combine(a + 1, b - 1)
        and can_combine(b, j)
        for a, b in get_valid_splits(i, j)
    )

    return memo[i, j]


N = int(input())
BALLS = list(map(int, input().split()))

CUM = list(accumulate(BALLS))

memo = {}

print(max(
    query_sum(i, j)
    for i in range(N)
    for j in range(i, N)
    if can_combine(i, j)
))
