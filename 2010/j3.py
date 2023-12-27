d = {"A": 0, "B": 0}

while True:
    lol = input().split()
    if lol[0] == "1":
        d[lol[1]] = int(lol[2])
    elif lol[0] == "2":
        print(d[lol[1]])
    elif lol[0] == "3":
        d[lol[1]] += d[lol[2]]
    elif lol[0] == "4":
        d[lol[1]] *= d[lol[2]]
    elif lol[0] == "5":
        d[lol[1]] -= d[lol[2]]
    elif lol[0] == "6":
        d[lol[1]] /= d[lol[2]]
        d[lol[1]] = int(d[lol[1]])
    else:
        break
