def calc_walking_time(c, p, w, d):
    distance = max(0, abs(p - c) - d)
    return distance * w


N = int(input())

FRIENDS = [
    tuple(map(int, input().split()))
    for _ in range(N)
]

print(min(
    sum(calc_walking_time(c, *friend) for friend in FRIENDS)
    for c in range(2001)
))
