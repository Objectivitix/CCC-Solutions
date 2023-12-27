digits = [
    int(input())
    for _ in range(4)
]

print(
    "ignore"
    if (
        digits[0] in (8, 9)
        and digits[1] == digits[2]
        and digits[3] in (8, 9)
    )
    else "answer"
)
