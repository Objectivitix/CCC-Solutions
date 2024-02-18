N, M, K = map(int, input().split())

assert M == 2

if not N <= K < N * 2:
    print("-1")
    raise SystemExit

diff = K - N

beginning_pairs_n = diff // 2
beginning = "12" * beginning_pairs_n

middle = "1" * (N - 1 - beginning_pairs_n * 2)
end = "2" if diff & 1 else "1"

piece = f"{beginning}{middle}{end}"

print(" ".join(list(piece)))
