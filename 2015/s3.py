from bisect import bisect_left

G = int(input())
P = int(input())

available = list(range(1, G + 1))
total = 0

for _ in range(P):
    g = int(input())

    dock_at = bisect_left(available, g)

    if dock_at == G - total or available[dock_at] > g:
        dock_at -= 1

    if dock_at < 0:
        break

    total += 1
    del available[dock_at]

print(total)
