_ = input()
pairs = zip(input().split(), input().split())

valid_pairs = set()

for pair in pairs:
    if frozenset(pair) in valid_pairs:
        continue

    if pair[0] == pair[1]:
        print("bad")
        raise SystemExit

    for v_pair in valid_pairs:
        if pair[0] in v_pair or pair[1] in v_pair:
            print("bad")
            raise SystemExit

    valid_pairs.add(frozenset(pair))

print("good")
