n = int(input())

possets = [
    tuple(map(int, input().split(",")))
    for _ in range(n)
]

possets_sorted_by_x = sorted(possets, key=lambda posset: posset[0])
possets_sorted_by_y = sorted(possets, key=lambda posset: posset[1])

left = possets_sorted_by_x[0]
right = possets_sorted_by_x[-1]
top = possets_sorted_by_y[-1]
bottom = possets_sorted_by_y[0]

print(left[0] - 1, bottom[1] - 1, sep=",")
print(right[0] + 1, top[1] + 1, sep=",")
