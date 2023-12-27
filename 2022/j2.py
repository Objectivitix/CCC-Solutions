n = int(input())

players = (
    (int(input()), int(input()))
    for _ in range(n)
)

number = sum(player[0] * 5 - player[1] * 3 > 40 for player in players)
gold = number == n

print(
    str(number)
    + ("+" if gold else "")
)
