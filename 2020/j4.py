def get_cyclic_shifts(string):
    for i, _ in enumerate(string):
        yield string[i:] + string[:i]

t = input()
s = input()

for cyclic_shift in get_cyclic_shifts(s):
    if t.find(cyclic_shift) != -1:
        print("yes")
        raise SystemExit

print("no")
