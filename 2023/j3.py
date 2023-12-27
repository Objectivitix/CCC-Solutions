n = int(input())

people = list(zip(*(
    input()
    for _ in range(n)
)))

most = 0

for i, p in enumerate(people):
    c = "".join(p).count("Y")

    if c > most:
        most = c

indices = []

for i, p in enumerate(people):
    c = "".join(p).count("Y")

    if c == most:
        indices.append(i + 1)

print(",".join(map(str, indices)))
