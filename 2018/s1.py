N = int(input())

V = sorted(
    int(input())
    for _ in range(N)
)

minimum = min(
    (b + c) / 2 - (a + b) / 2
    for a, b, c in zip(V, V[1:], V[2:])
)

print(f"{minimum:.1f}")
