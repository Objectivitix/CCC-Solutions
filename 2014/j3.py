n = int(input())
dice_rolls = (
    map(int, input().split())
    for _ in range(n)
)

alice = 100
david = 100

for alice_roll, david_roll in dice_rolls:
    if alice_roll == david_roll:
        continue

    if alice_roll > david_roll:
        david -= alice_roll
    else:
        alice -= david_roll

print(alice)
print(david)
