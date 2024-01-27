W = int(input())
N = int(input())

def get_squads(weights):
    yield weights[:1] 
    yield weights[:2]
    yield weights[:3] 
    yield from zip(weights, weights[1:], weights[2:], weights[3:])

weights = [int(input()) for _ in range(N)]
bridged = 0

for squad in get_squads(weights):
    if sum(squad) > W:
        break

    bridged += 1

print(bridged)
