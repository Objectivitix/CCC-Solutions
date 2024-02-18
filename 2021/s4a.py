import sys
from collections import defaultdict, deque


def input_ints():
    return map(int, sys.stdin.readline().split())


def get_min_dists_to_school(adjs, school):
    dist = {school: 0}
    dq = deque([school])

    while dq:
        curr = dq.popleft()

        for adj in adjs[curr]:
            tentative = dist[curr] + 1

            if tentative < dist.get(adj, float("inf")):
                dist[adj] = tentative
                dq.append(adj)

    return dist


def parse_raw():
    n, w, d = input_ints()

    adjs = defaultdict(list)

    for _ in range(w):
        u, v = input_ints()

        # Inverting dir so we can BFS *from* school.
        adjs[v].append(u)

    route = input_ints()

    return get_min_dists_to_school(adjs, n), list(route), d


MIN_DISTS_TO_SCHOOL, route, D = parse_raw()

for _ in range(D):
    x, y = input_ints()

    i, j = x - 1, y - 1
    route[i], route[j] = route[j], route[i]

    print(min(
        time_on_subway + MIN_DISTS_TO_SCHOOL.get(station, float("inf"))
        for time_on_subway, station in enumerate(route)
    ))
