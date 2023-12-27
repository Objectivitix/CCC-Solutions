b = int(input())

p = 5 * b - 400
sea = (
    -1 if p > 100 else
    1 if p < 100 else
    0
)

print(p)
print(sea)
