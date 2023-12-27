n = int(input())

count = 0

for y in range(n // 5 + 1):
    x = (n - 5 * y) / 4

    if x.is_integer():
        count += 1

print(count)
