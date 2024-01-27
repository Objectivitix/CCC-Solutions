# http://mmhs.ca/ccc/2013/ccc2013s5.txt
# Dijkstra is so overkill.
# Forward DP, still O(N √N), but I like this solution
# a lot so including it here.

from math import floor, inf, sqrt


def get_all_factor_pairs(n):
    yield (1, n)

    for i in range(2, floor(sqrt(n)) + 1):
        tentative = n / i

        if tentative.is_integer():
            yield (i, int(tentative))


N = int(input())

# dp[i] = min cost to get from 1 to i + 1
dp = [inf for _ in range(N)]
dp[0] = 0

for i in range(N):
    for a, b in get_all_factor_pairs(i + 1):
        for step, cost in ((a, b), (b, a)):
            if i + step >= N:
                continue

            dp[i + step] = min(dp[i] + cost, dp[i + step])

print(dp[N - 1])
