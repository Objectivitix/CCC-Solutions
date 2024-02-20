import math
from collections import defaultdict, deque
from copy import deepcopy

N, E, S, W = (-1, 0), (0, 1), (1, 0), (0, -1)

OUT_DELTAS = {
    "S": [N, E, S, W],
    ".": [N, E, S, W],
    "U": [N],
    "R": [E],
    "D": [S],
    "L": [W],
}

CONVEYORS = "URDL"


def raycast(i, j, maze):
    for di, dj in (N, E, S, W):
        new_i, new_j = i + di, j + dj

        while maze[new_i][new_j] != "W":
            if maze[new_i][new_j] in "S.": # this is brutal guys what the flip
                maze[new_i][new_j] = "#"

            new_i += di
            new_j += dj

    maze[i][j] = "#"


def wallify_cameras(maze):
    for i, row in enumerate(maze):
        for j, char in enumerate(row):
            if char == "C":
                raycast(i, j, maze)

    for i, row in enumerate(maze):
        for j, char in enumerate(row):
            if char in "#":
                maze[i][j] = "W"


def get_adjs(i, j, deltas, no_camera_maze):
    for di, dj in deltas:
        if no_camera_maze[i + di][j + dj] != "W":
            yield i + di, j + dj


def get_adj_list(no_camera_maze):
    adj_list = defaultdict(list)

    for i, row in enumerate(no_camera_maze):
        for j, char in enumerate(row):
            if char == "W":
                continue

            for adj in get_adjs(i, j, OUT_DELTAS[char], no_camera_maze):
                adj_list[i, j].append(adj)

    return adj_list


def parse_raw():
    n, _ = map(int, input().split())

    maze = []
    targets = []

    for i in range(n):
        row = list(input())
        maze.append(row)

        for j, char in enumerate(row):
            if char == ".":
                targets.append((i, j))

            if char == "S":
                yield (i, j)

    yield targets
    yield deepcopy(maze)

    wallify_cameras(maze)

    yield get_adj_list(maze)


START, TARGETS, MAZE, ADJ_LIST = parse_raw()

dist = defaultdict(lambda: float("inf"))
dq = deque([START])

dist[START] = 0

while dq:
    curr = dq.popleft()
    cell = MAZE[curr[0]][curr[1]]

    for adj in ADJ_LIST[curr]:
        alt_dist = dist[curr] + (cell not in CONVEYORS)

        if alt_dist < dist[adj]:
            dist[adj] = alt_dist
            dq.append(adj)

for target in TARGETS:
    min_path = dist[target]

    if math.isinf(min_path):
        print(-1)
        continue

    print(min_path)
