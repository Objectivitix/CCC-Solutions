GROUPS = {
    0: -1,
    1: 3,
    2: 3,
    3: 2,
    4: 2,
    5: 1,
    6: 1,
}

results = [
    input()
    for _ in range(6)
]

print(GROUPS["".join(results).count("W")])
