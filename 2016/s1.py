from collections import Counter

a = Counter(input())
b = Counter(input())

del b["*"]

# The wonders of 3.10 ...
# Why does CCCGrader have to be stuck in 3.6? 😩
#
# print("A" if a >= b else "N")

from string import ascii_lowercase

valid = all(
    b[letter] <= a[letter]
    for letter in ascii_lowercase
)

print("A" if valid else "N")
