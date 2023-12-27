tests = []

while True:
    inp = input()

    if inp == "0":
        break

    _, *data = inp.split()

    diffs = [int(b) - int(a) for a, b in zip(data[:-1], data[1:])]
    tests.append(diffs)

for test in tests:
    if not test:
        print(0)
        continue

    for i, _ in enumerate(test, 1):
        candidate = test[0:i]
        length = len(test)

        valid = True
        for offset in range(0, length // i, i):
            if test[offset:offset + i] != candidate:
                valid = False
                continue

        rest = test[offset + i:]
        for item1, item2 in zip(candidate, rest):
            if item1 != item2:
                valid = False

        if valid:
            break

    print(i)
