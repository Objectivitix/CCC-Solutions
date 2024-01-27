Y = int(input())
tentative = Y + 1

while True:
    s = str(tentative)
    if len(set(s)) == len(s):
        break

    tentative += 1

print(tentative)
