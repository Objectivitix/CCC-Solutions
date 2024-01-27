# Graph processing optimised using a modified version
# of the Sieve of Eratosthenes. The bottleneck lies in
# the |E| term of Dijkstra's worst-case complexity,
# which is still O(N √N). I thought I could maybe
# squeeze out a point or two regardless, but the later
# cases wouldn't budge. Still 8/15 points.

from collections import defaultdict
from math import floor, inf, sqrt
from queue import PriorityQueue


def get_all_factor_pairs_of_each_num(n):
    factor_pairs = defaultdict(list)

    for i in range(2, floor(sqrt(n)) + 1):
        for j, k in enumerate(range(i ** 2, n + 1, i), i):
            factor_pairs[k].append((i, j))

    for k in range(1, n + 1):
        factor_pairs[k].append((1, k))

    return factor_pairs


N = int(input())
FACTOR_PAIRS = get_all_factor_pairs_of_each_num(N)

pq = PriorityQueue()
pq.put((0, 1))

dist = defaultdict(lambda: inf)
dist[1] = 0

while not pq.empty():
    _, curr = pq.get()

    if curr == N:
        break

    for a, b in FACTOR_PAIRS[curr]:
        for neighbor, weight in ((curr + a, b), (curr + b, a)):
            tentative = dist[curr] + weight

            if tentative < dist[neighbor]:
                dist[neighbor] = tentative
                pq.put((tentative, neighbor))

print(dist[N])
