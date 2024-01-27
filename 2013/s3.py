from itertools import combinations, product

TEAMS = "1234"
GAMES = set(combinations(TEAMS, 2))
STATES = [(3, 0), (1, 1), (0, 3)]


def parse_raw():
    yield input()

    g = int(input())

    scores = {team: 0 for team in TEAMS}
    played = set()

    for _ in range(g):
        # a < b guaranteed
        a, b, s_a, s_b = input().split()
        played.add((a, b))

        s_a, s_b = int(s_a), int(s_b)
        da, db = STATES[0 if s_a > s_b else 1 if s_a == s_b else 2]

        scores[a] += da
        scores[b] += db

    yield scores
    yield GAMES - played


FAV, CURR_SCORES, GAMES_LEFT = parse_raw()
OTHERS = set(TEAMS) - {FAV}

total = 0

for tourney in product(STATES, repeat=len(GAMES_LEFT)):
    scores = CURR_SCORES.copy()

    for (a, b), (da, db) in zip(GAMES_LEFT, tourney):
        scores[a] += da
        scores[b] += db

    if all(scores[FAV] > scores[other] for other in OTHERS):
        total += 1

print(total)
