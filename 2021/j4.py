# O(n^2) sol, where n is length of string

CONVERSION = {"L": 3, "M": 2, "S": 1}

def is_fronted(string, prefix):
    it = iter(string)

    if next(it) != prefix:
        return False

    continuing = True

    for char in it:
        if char != prefix:
            continuing = False
            continue

        if char == prefix and not continuing:
            return False

    return True

def swap(string, index1, index2):
    return (
        string[:index1]
        + string[index2]
        + string[index1 + 1: index2]
        + string[index1]
        + string[index2 + 1:]
    )

def get_left(string, no):
    for i, char in enumerate(string):
        if char != no:
            return i

def get_swaps(string):
    if len(set(string)) == 1:
        return 0

    swaps_n = 0

    highest = max(string, key=lambda char: CONVERSION[char])

    while not is_fronted(string, str(highest)):
        left = get_left(string, highest)
        right = string.rfind(highest)
        string = swap(string, left, right)
        swaps_n += 1

    swaps_n += get_swaps(string[string.rfind(highest) + 1:])
    return swaps_n

print(get_swaps(input()))
