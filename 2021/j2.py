n = int(input())

auction = [
    (input(), int(input()))
    for _ in range(n)
]

auction_sorted = sorted(
    auction,
    key=lambda entry: entry[1],
    reverse=True,
)

print(auction_sorted[0][0])
