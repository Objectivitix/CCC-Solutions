# http://mmhs.ca/ccc/2014/2014S4SweepLineCalvinLiu.txt
# Sweep line is pretty. Darn. Cool.

N = int(input())
THRESHOLD = int(input())

edges = []
ys = set()

for _ in range(N):
    x1, y1, x2, y2, tint = map(int, input().split())

    edges.append((x1, y1, y2, tint))
    edges.append((x2, y1, y2, -tint))  # mindblowing

    ys.add(y1)
    ys.add(y2)

sorted_edges = sorted(edges)
sorted_ys = sorted(ys)

curr_y_tints = {y: 0 for y in sorted_ys}
total = 0

for i, (x, y1, y2, tint) in enumerate(sorted_edges):
    for j, y in enumerate(sorted_ys):
        if curr_y_tints[y] >= THRESHOLD:
            width = x - sorted_edges[i - 1][0]
            height = sorted_ys[j + 1] - y
            total += width * height

    for y in sorted_ys:
        if y1 <= y < y2:
            curr_y_tints[y] += tint

print(total)
