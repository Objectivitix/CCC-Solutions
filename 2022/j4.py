from collections import defaultdict

together = defaultdict(list)
apart = defaultdict(list)

x = int(input())

for _ in range(x):
    a, b = input().split()
    together[a].append(b)
    together[b].append(a)

y = int(input())

for _ in range(y):
    a, b = input().split()
    apart[a].append(b)
    apart[b].append(a)

g = int(input())

count = 0
together_counted = defaultdict(lambda: defaultdict(lambda: False))
apart_counted = defaultdict(lambda: defaultdict(lambda: False))

for _ in range(g):
    group = input().split()

    for student in group:
        for t_constraint in together[student]:
            if not together_counted[t_constraint][student] and t_constraint not in group:
                count += 1
                together_counted[student][t_constraint] = True
        for a_constraint in apart[student]:
            if not apart_counted[a_constraint][student] and a_constraint in group:
                count += 1
                apart_counted[student][a_constraint] = True

print(count)
