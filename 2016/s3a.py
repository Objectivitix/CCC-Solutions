# Naive O(N*M^2 + M!) solution.
#
# We take advantage of the constraint M <= 8 for the
# first 9 points. We BFS the shortest path between all
# target pairs (yielding a complete graph), then
# minimize over all permutations.

from collections import defaultdict, deque
from itertools import combinations, permutations, tee


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def parse_raw():
    n, m = map(int, input().split())

    yield n
    yield m

    yield input().split()

    adj_list = defaultdict(list)

    for _ in range(n - 1):
        a, b = input().split()
        adj_list[a].append(b)
        adj_list[b].append(a)

    yield adj_list


def find_shortest_path(source, target, adj_list):
    visited = set()
    dq = deque([(source, 0)])

    while dq:
        curr, length = dq.popleft()

        if curr in visited:
            continue

        visited.add(curr)

        if curr == target:
            return length

        for adj in adj_list[curr]:
            dq.append((adj, length + 1))

    return -1


_, _, TARGETS, ADJ_LIST = parse_raw()

graph = defaultdict(dict)

for a, b in combinations(TARGETS, 2):
    length = find_shortest_path(a, b, ADJ_LIST)
    graph[a][b] = length
    graph[b][a] = length

print(min(
    sum(graph[a][b] for a, b in pairwise(seq))
    for seq in permutations(TARGETS)
))
