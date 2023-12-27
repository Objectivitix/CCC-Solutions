def tree_in_square(tree_pos, top_left_pos, side_length):
    return (
        top_left_pos[0] <= tree_pos[0] < top_left_pos[0] + side_length
        and top_left_pos[1] <= tree_pos[1] < top_left_pos[1] + side_length
    )

n = int(input())

t = int(input())
trees = [
    tuple(map(int, input().split()))
    for _ in range(t)
]

m = 0

for side_length in range(1, n + 1):
    for i in range(1, n - side_length + 2):
        for j in range(1, n - side_length + 2):

            valid = True
            for tree in trees:
                if tree_in_square(tree, (i, j), side_length):
                    valid = False
                    break

            if valid:
                m = max(m, side_length)

print(m)
