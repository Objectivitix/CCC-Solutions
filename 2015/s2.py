SIZES = {
    "TAKEN": -1,
    "S": 0,
    "M": 1,
    "L": 2,
}

J = int(input())
A = int(input())

JERSEYS = [input() for _ in range(J)]

good = 0

for _ in range(A):
    size, index = input().split()
    index = int(index) - 1

    if SIZES[JERSEYS[index]] < SIZES[size]:
        continue

    good += 1
    JERSEYS[index] = "TAKEN"

print(good)
