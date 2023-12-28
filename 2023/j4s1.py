DELTAS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# def get_neighboring_tiles(tile_y, tile_x, mat, height, width):
#     for dy, dx in DELTAS:
#         new_y, new_x = tile_y + dy, tile_x + dx
#         if 0 <= new_y < height and 0 <= new_x < width:
#             yield mat[new_y][new_x]

def neighbors(ty, tx, mat, width):
    if 0 <= tx - 1:
        yield mat[ty][tx - 1]
    if tx + 1 < width:
        yield mat[ty][tx + 1]
    if (tx - 1) & 1:
        if ty == 0:
            yield mat[1][tx]
        else:
            yield mat[0][tx]

_ = input()

tiles = [
    list(map(int, input().split()))
    for _ in range(2)
]
h = len(tiles)
w = len(tiles[0])

wet_areas_n = 0
overlapping_edges_n = 0

for i, row in enumerate(tiles):
    for j, tile in enumerate(row):
        if tile == 0:
            continue

        wet_areas_n += 1

        for n_tile in neighbors(i, j, tiles, w):
            if n_tile == 1:
                overlapping_edges_n += 1

print(wet_areas_n * 3 - overlapping_edges_n)
