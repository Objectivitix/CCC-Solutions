from enum import Enum

class Header(Enum):
    LEFT = 0
    RIGHT = 1
    AS_PREV = 2

def parse_header(digit1, digit2):
    s = int(digit1) + int(digit2)

    if s & 1:
        return Header.LEFT
    elif s == 0:
        return Header.AS_PREV
    else:
        return Header.RIGHT

direction = None

while True:
    instruction = input()

    if instruction == "99999":
        break

    digit1, digit2, *rest = instruction

    if parse_header(digit1, digit2) == Header.LEFT:
        direction = "left"
    elif parse_header(digit1, digit2) == Header.RIGHT:
        direction = "right"
    else:
        pass  # direction stays the same = as previous

    print(direction, "".join(rest))
