def is_palindrome(s):
    return s == s[::-1]

string = input()
length = len(string)
lp_length = 0

for i in range(length):
    for j in range(i, length + 1):
        substring = string[i:j]

        if not substring:
            continue

        if is_palindrome(substring):
            lp_length = max(lp_length, len(substring))

print(lp_length)
