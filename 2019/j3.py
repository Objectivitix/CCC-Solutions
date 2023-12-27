n = int(input())

for _ in range(n):
    counter = []
    line_it = iter(input())

    prev_char = next(line_it)
    curr_count = 1

    for char in line_it:
        if char != prev_char:
            counter.append((prev_char, curr_count))
            curr_count = 1
        else:
            curr_count += 1
        prev_char = char

    counter.append((prev_char, curr_count))

    print(" ".join(f"{count} {char}" for char, count in counter))
