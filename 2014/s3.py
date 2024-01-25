from collections import deque


def ensures_peace_and_posterity(mountain):
    branch = deque()
    latest = 0

    while mountain:
        from_mountain = mountain.pop()

        if from_mountain == latest + 1:
            latest += 1
            continue

        if not branch:
            branch.append(from_mountain)
            continue

        from_branch = branch[0]

        if from_branch == latest + 1:
            latest += 1
            branch.popleft()
            continue

        if from_mountain > from_branch:
            return False

        branch.append(from_mountain)

    return True


T = int(input())

for _ in range(T):
    n = int(input())
    mountain = [int(input()) for _ in range(n)]

    print("Y" if ensures_peace_and_posterity(mountain) else "N")
