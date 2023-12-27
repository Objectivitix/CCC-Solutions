RULE_VIOLATIONS_TO_ROTATIONS = {
    (True, True): 0,
    (False, True): 90,
    (False, False): 180,
    (True, False): 270,
}

def rotate_matrix_clockwise(mat, degrees):
    if degrees == 0:
        return mat

    if degrees == 90:
        return reversed(list(zip(*mat)))

    if degrees == 180:
        return reversed([reversed(row) for row in mat])

    if degrees == 270:
        return (reversed(row) for row in zip(*mat))

n = int(input())

mat = [
    [int(num) for num in input().split()]
    for _ in range(n)
]

rows_correct = mat[0] == sorted(mat[0])

first_column = list(next(zip(*mat)))
columns_correct = first_column == sorted(first_column)

rotation = RULE_VIOLATIONS_TO_ROTATIONS[(rows_correct, columns_correct)]

for row in rotate_matrix_clockwise(mat, rotation):
    print(" ".join(map(str, row)))
