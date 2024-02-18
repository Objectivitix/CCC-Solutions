N, M, k = map(int, input().split())

piece = []

for i in range(N):
    remaining = N - i - 1
    curr = min(k - remaining, M)

    if curr <= 0:
        break

    if curr > i:
        next_pitch = min(M, i + 1)
        k -= next_pitch
    else:
        next_pitch = piece[i - curr]
        k -= curr

    piece.append(next_pitch)

if k == 0 and len(piece) == N:
    print(" ".join(map(str, piece)))
else:
    print("-1")
