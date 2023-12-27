MOVEMENTS = {
    "A": {"V": "B", "H": "C"},
    "B": {"V": "A", "H": "D"},
    "C": {"V": "D", "H": "A"},
    "D": {"V": "C", "H": "B"},
}

number_pos = {
    1: "A",
    2: "B",
    3: "C",
    4: "D",
}

for char in input():
    for number, pos in number_pos.items():
        number_pos[number] = MOVEMENTS[pos][char]

pos_number = {
    pos: number
    for number, pos in number_pos.items()
}

print(pos_number["A"], pos_number["B"])
print(pos_number["C"], pos_number["D"])
