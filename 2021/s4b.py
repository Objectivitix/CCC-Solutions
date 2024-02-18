import itertools
import sys
from collections import defaultdict, deque
from heapq import *


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

pq = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = '<removed-task>'      # placeholder for a removed task
counter = itertools.count()     # unique sequence count

def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heappush(pq, entry)

def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return priority, task
    raise KeyError('pop from an empty priority queue')

for time_on_subway, station in enumerate(route):
    add_task(station, time_on_subway + MIN_DISTS_TO_SCHOOL.get(station, float("inf")))

# print(pq)

for _ in range(D):
    x, y = input_ints()

    i, j = x - 1, y - 1
    a, b = route[i], route[j]

    add_task(a, j + MIN_DISTS_TO_SCHOOL.get(a, float("inf")))
    add_task(b, i + MIN_DISTS_TO_SCHOOL.get(b, float("inf")))

    route[i], route[j] = route[j], route[i]

    # print(pq)
    dist, station = pop_task()
    print(dist)

    add_task(station, dist)
    # print(pq)
