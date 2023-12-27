a_3 = int(input())
a_2 = int(input())
a_1 = int(input())

b_3 = int(input())
b_2 = int(input())
b_1 = int(input())

a_score = a_3 * 3 + a_2 * 2 + a_1
b_score = b_3 * 3 + b_2 * 2 + b_1

print(
    "A" if a_score > b_score else
    "B" if a_score < b_score else
    "T"
)
