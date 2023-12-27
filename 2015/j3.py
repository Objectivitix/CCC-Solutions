VOWELS = "aeiou"

word = input()

new_word = []

for char in word:
    if char in VOWELS:
        new_word.append(char)
        continue

    new_word.append(char)

    # We take advantage of stable sorting.
    distances = sorted(VOWELS, key=lambda vowel: abs(ord(char) - ord(vowel)))
    new_word.append(distances[0])

    if char == "z":
        new_word.append("z")
        continue

    next_letter = chr(ord(char) + 1)
    if next_letter in VOWELS:
        next_letter = chr(ord(char) + 2)

    new_word.append(next_letter)

print("".join(new_word))
