# O(N √N) factor-graph & Dijkstra's solution.
# Gets 8/15 points.

from collections import defaultdict
from math import floor, inf, sqrt
from queue import PriorityQueue


def get_all_factor_pairs(n):
    yield (1, n)

    for i in range(2, floor(sqrt(n)) + 1):
        tentative = n / i

        if tentative.is_integer():
            yield (i, int(tentative))


def parse_raw():
    n = int(input())

    adj_list = defaultdict(list)

    for i in range(1, n):
        for a, b in get_all_factor_pairs(i):
            adj_list[i].append((i + a, b))

            if a != b:
                adj_list[i].append((i + b, a))

    return n, adj_list


TARGET, ADJS = parse_raw()

pq = PriorityQueue()
pq.put((0, 1))

dist = defaultdict(lambda: inf)
dist[1] = 0

while not pq.empty():
    _, curr = pq.get()

    if curr == TARGET:
        break

    for neighbor, weight in ADJS[curr]:
        tentative = dist[curr] + weight

        if tentative < dist[neighbor]:
            dist[neighbor] = tentative
            pq.put((tentative, neighbor))

print(dist[TARGET])
