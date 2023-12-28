_ = input()
a = map(int, input().split())
b = map(int, input().split())

a_cum = 0
b_cum = 0
ks = [0]

for k, (i, j) in enumerate(zip(a, b), start=1):
    a_cum += i
    b_cum += j

    if a_cum == b_cum:
        ks.append(k)

print(max(ks))
