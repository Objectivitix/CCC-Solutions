import re

def get_tentative_next_steps(rules, curr):
    for i, (rule_input, rule_output) in enumerate(rules, start=1):
        length = len(rule_input)

        for occurence in re.finditer(rf"(?=({rule_input}))", curr):
            start = occurence.start()
            end = start + length

            yield (
                i,
                start + 1,
                curr[:start] + rule_output + curr[end:],
            )

def find_moves(rules, curr, goal, steps_left, prev_step):
    if steps_left == 0:
        if curr == goal:
            steps.append(prev_step)
            return True
        else:
            return False

    for tentative in get_tentative_next_steps(rules, curr):
        next_string = tentative[2]

        if (next_string, steps_left) in memo:
            continue

        memo.add((next_string, steps_left))

        if find_moves(rules, next_string, goal, steps_left - 1, tentative):
            steps.append(prev_step)
            return True

    return False

substitution_rules = tuple(
    tuple(input().split())
    for _ in range(3)
)

total_steps_n, initial, goal = input().split()
total_steps_n = int(total_steps_n)

steps = []  # global var modified by find_moves
memo = set()  # global var used to speedy speedy

find_moves(substitution_rules, initial, goal, total_steps_n, None)

for step in reversed(steps):
    if step == None:
        continue

    print(" ".join(map(str, step)))
