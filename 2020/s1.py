from itertools import tee

def pairwise(iterable):
    a, b = tee(iterable)
    next(b)

    return zip(a, b)

n = int(input())

observations = sorted(
    tuple(map(int, input().split()))
    for _ in range(n)
)

speeds = (
    abs(position_b - position_a) / (time_b - time_a)
    for (time_a, position_a), (time_b, position_b) in pairwise(observations)
)

print(max(speeds))
