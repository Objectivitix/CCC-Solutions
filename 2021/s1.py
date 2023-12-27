from itertools import tee

def pairwise(iterable):
    a, b = tee(iterable)
    next(b)

    return zip(a, b)

_ = input()

heights = pairwise(map(int, input().split()))
widths = map(int, input().split())

area = sum(
    (h1 + h2) * w / 2
    for (h1, h2), w in zip(heights, widths)
)

if area.is_integer():
    area = int(area)

print(area)
