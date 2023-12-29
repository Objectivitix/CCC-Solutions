# Gets 11/15 points.

import sys
from collections import defaultdict, deque

m = int(input())
n = int(input())

maze = (
    map(int, line.split())
    for line in sys.stdin.read().splitlines()
)

adjacencies = defaultdict(list)

for i, row in enumerate(maze, start=1):
    for j, value in enumerate(row, start=1):
        adjacencies[value].append((i, j))

start = (m, n)
end = (1, 1)

visited = set()
dq = deque([start])

while dq:
    curr = dq.popleft()

    if curr == end:
        print("yes")
        raise SystemExit

    visited.add(curr)

    for neighbor in adjacencies[curr[0] * curr[1]]:
        if neighbor not in visited:
            dq.append(neighbor)

print("no")
