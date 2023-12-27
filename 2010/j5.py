from collections import deque

def get_all_moves(x, y):
    yield x + 1, y + 2
    yield x + 2, y + 1
    yield x + 2, y - 1
    yield x + 1, y - 2
    yield x - 1, y - 2
    yield x - 2, y - 1
    yield x - 2, y + 1
    yield x - 1, y + 2

def get_possible_moves(x, y):
    for new_x, new_y in get_all_moves(x, y):
        if 0 <= new_x < 8 and 0 <= new_y < 8:
            yield new_x, new_y

knight_moves = {}
dist = {}

for y in range(8):  # in the problem, y goes up, but symmetry so idc :D
    for x in range(8):
        knight_moves[(x, y)] = list(get_possible_moves(x, y))
        dist[(x, y)] = float("inf")

start_node = tuple(int(p) - 1 for p in input().split())  # 1-indexed smh
end_node = tuple(int(p) - 1 for p in input().split())

dq = deque([start_node])
dist[start_node] = 0

while dq:
    curr_node = dq.popleft()

    if curr_node == end_node:
        print(dist[curr_node])
        break

    for neighbor in knight_moves[curr_node]:
        dist[neighbor] = dist[curr_node] + 1
        dq.append(neighbor)
