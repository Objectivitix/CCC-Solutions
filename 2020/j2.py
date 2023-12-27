p = int(input())
n = int(input())
r = int(input())

if r == 1:
    i = 0
    while n * (i + 1) <= p:
        i += 1

    print(i)
    raise SystemExit

i = 0
while n * (r ** (i + 1) - 1) / (r - 1) <= p:
    i += 1

print(i)
