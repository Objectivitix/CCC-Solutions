# I SOLVED A S5 HOLY COW (used a hint but WHO CARES)!!!
#
# Line sweep for initial LCM calculations in linear time
# + sparse table for range GCD queries (to check validity
# of tentative solution) in constant time (per query).
#
# Time: O(N + M)    Space: O(N + M + max(Z_i))

from collections import Counter
from math import floor, gcd, lcm, log2


def build_gcd_sparse_table(arr):
    length = len(arr)
    table = [arr.copy()]

    for i in range(1, floor(log2(length)) + 1):
        row = []

        for j in range(length - 2 ** i + 1):
            row.append(gcd(
                table[i - 1][j],
                table[i - 1][j + 2 ** (i - 1)],
            ))

        table.append(row)

    return table


N, M  = map(int, input().split())

queries = []  # for final checking

requirements = []  # for line sweep

for _ in range(M):
    x, y, z = map(int, input().split())
    queries.append((x, y, z))

    requirements.append((x, 1, z))
    requirements.append((y + 1, -1, z))

divisors = Counter()
curr_lcm = 1
prev_pos = 1
lcms = []

for pos, sign, divisor in sorted(requirements):
    for _ in range(prev_pos, pos):
        lcms.append(curr_lcm)

    if sign == 1:
        divisors[divisor] += 1
    else:
        divisors[divisor] -= 1

    curr_lcm = lcm(*(+divisors).keys())
    prev_pos = pos

for _ in range(pos, N + 1):
    lcms.append(1)

table = build_gcd_sparse_table(lcms)

for x, y, z in queries:
    l = x - 1
    r = y - 1

    if l == r:
        if lcms[l] != z:
            print("Impossible")
            raise SystemExit
        else:
            continue

    s = r - l + 1
    i = floor(log2(s))

    if gcd(table[i][l], table[i][r - 2 ** i + 1]) != z:
        print("Impossible")
        raise SystemExit

print(" ".join(map(str, lcms)))
