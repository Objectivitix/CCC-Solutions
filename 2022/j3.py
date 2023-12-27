import re

HARP_TUNING_REGEX = r"([A-Z]+)([+-])(\d+)"

inp = input()

matches = re.findall(HARP_TUNING_REGEX, inp)

for harp_strings, operation, turns in matches:
    print(
        harp_strings,
        "tighten" if operation == "+" else "loosen",
        turns,
    )
