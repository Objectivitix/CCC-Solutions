from math import ceil

n = int(input())

s = 0
for i in range(n, ceil(n / 2) - 1, -1):
    if i <= 5:
        s += 1

print(s)
