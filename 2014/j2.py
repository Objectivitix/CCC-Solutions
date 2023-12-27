_ = input()
votes = input()

votes_for_a = votes.count("A")
votes_for_b = votes.count("B")

print(
    "A" if votes_for_a > votes_for_b else
    "B" if votes_for_a < votes_for_b else
    "Tie"
)
