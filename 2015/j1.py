month = int(input())
day = int(input())

print(
    "Before" if (month, day) < (2, 18) else
    "After" if (month, day) > (2, 18) else
    "Special"
)
