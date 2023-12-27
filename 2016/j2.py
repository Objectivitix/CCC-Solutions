mat = [
    tuple(map(int, input().split()))
    for _ in range(4)
]

mat_other_way = list(zip(*mat))

magic_sum = sum(mat[0])

print(
    "magic"
    if (
        all(sum(row) == magic_sum for row in mat)
        and all(sum(column) == magic_sum for column in mat)
    )
    else "not magic"
)
