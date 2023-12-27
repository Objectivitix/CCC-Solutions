from itertools import accumulate

distances = [int(dist) for dist in input().split()]

for i in range(len(distances) + 1):
    a = accumulate(distances[i:])
    b = accumulate(distances[i - 1::-1]) if i - 1 >= 0 else []

    print(" ".join(map(str, list(b)[::-1] + [0] + list(a))))
