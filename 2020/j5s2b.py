# Gets 13/15 points.
#
# Performs slower on other cases, but passes Batch 5
# which grants two extra points. I think it's mere
# luck that the final case of Batch 5 is weak enough
# for this (very) slightly different implementation.
# I won't attempt to hack this further; this may well
# be one of those times where Python doesn't cut it.

from collections import deque


def parse_maze(m):
    grid = {}
    adjacencies = {}

    for i in range(1, m + 1):
        for j, value in enumerate(map(int, input().split()), start=1):
            grid[(i, j)] = value

            product = i * j

            if product in adjacencies:
                adjacencies[product].append((i, j))
            else:
                adjacencies[product] = [(i, j)]

    return grid, adjacencies


M = int(input())
N = int(input())

GRID, ADJ = parse_maze(M)

START = (1, 1)
END = (M, N)

visited = set()
dq = deque([START])

while dq:
    curr = dq.popleft()

    if curr == END:
        print("yes")
        raise SystemExit

    visited.add(curr)

    value = GRID[curr]

    if value not in ADJ:
        continue

    for neighbor in ADJ[value]:
        if neighbor not in visited:
            dq.append(neighbor)

print("no")
