from itertools import zip_longest
from math import ceil

n = int(input())
levels = sorted(map(int, input().split()))

split = ceil(n / 2)

lows, highs = levels[:split], levels[split:]

original = [
    str(measurement)
    for pair in zip_longest(reversed(lows), highs)
    for measurement in pair
    if measurement is not None
]

print(" ".join(original))
