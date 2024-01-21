def calc_walking_time(c, p, w, d):
    distance = max(0, abs(p - c) - d)
    return distance * w


def calc_walking_time_sum(c, friends):
    return sum(calc_walking_time(c, *friend) for friend in friends)


N = int(input())
P = 10 ** 9

FRIENDS = [
    tuple(map(int, input().split()))
    for _ in range(N)
]

low = 0
high = P

while low <= high:
    c = (low + high) // 2

    sum_at_c = calc_walking_time_sum(c, FRIENDS)
    sum_at_left = calc_walking_time_sum(c - 1, FRIENDS)
    sum_at_right = calc_walking_time_sum(c + 1, FRIENDS)

    if sum_at_left < sum_at_c:
        high = c - 1
        continue

    if sum_at_right < sum_at_c:
        low = c + 1
        continue

    break

print(sum_at_c)
