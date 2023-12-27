DELTAS_EIGHT = [
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
]

GET_THREE_DIRS = {
    (-1, 0): [(-1, 0), (0, -1), (0, 1)],
    (-1, 1): [(-1, 1), (-1, -1), (1, 1)],
    (0, 1): [(0, 1), (-1, 0), (1, 0)],
    (1, 1): [(1, 1), (-1, 1), (1, -1)],
    (1, 0): [(1, 0), (0, 1), (0, -1)],
    (1, -1): [(1, -1), (1, 1), (-1, -1)],
    (0, -1): [(0, -1), (1, 0), (-1, 0)],
    (-1, -1): [(-1, -1), (1, -1), (-1, 1)],
}

def get_neighbor(pos, deltas):
    y, x = pos
    dy, dx = deltas

    if 0 <= y + dy < ROWS_N and 0 <= x + dx < COLUMNS_N:
        return MAT[y + dy][x + dx], (y + dy, x + dx)

    return None, None

def word_hunt(curr_pos, index, av_dirs, last_dir):
    global occurrences_n

    if index == WORD_LENGTH - 1:  # entire word has been found
        occurrences_n += 1
        return

    target_letter = WORD[index + 1]
    av_dirs_n = len(av_dirs)

    for direction in av_dirs:
        adj_letter, adj_letter_pos = get_neighbor(curr_pos, direction)

        # if direction out of bounds or does not yield target, ignore
        if adj_letter is None or adj_letter != target_letter:
            continue

        # CASE 1: restrict to three directions now
        if av_dirs_n == 8:
            word_hunt(adj_letter_pos, index + 1, GET_THREE_DIRS[direction], direction)

        # CASE 2: we are past the start
        elif av_dirs_n == 3:
            if last_dir == direction:  # CASE 2a: no turning yet, continue with three directions
                word_hunt(adj_letter_pos, index + 1, GET_THREE_DIRS[direction], direction)
            else:  # CASE 2b: turned! one direction only now
                word_hunt(adj_letter_pos, index + 1, [direction], direction)

        # CASE 3: has already turned but has not reached end
        else:
            word_hunt(adj_letter_pos, index + 1, [direction], direction)

WORD = input()
WORD_LENGTH = len(WORD)

ROWS_N = int(input())
COLUMNS_N = int(input())

MAT = [
    input().split()
    for _ in range(ROWS_N)
]

occurrences_n = 0

for i, row in enumerate(MAT):
    for j, letter in enumerate(row):
        if letter == WORD[0]:
            word_hunt((i, j), 0, DELTAS_EIGHT, None)

print(occurrences_n)
