from collections import defaultdict, deque


def parse_raw():
    _, m = map(int, input().split())

    adj_list = defaultdict(list)

    for _ in range(m):
        u, v = input().split()
        adj_list[u].append(v)

    p, q = input().split()

    return adj_list, p, q


def exists_path(u, v, adj_list):
    visited = set()
    dq = deque([u])

    while dq:
        curr = dq.popleft()

        if curr == v:
            return True

        if curr in visited:
            continue

        visited.add(curr)

        dq += adj_list[curr]

    return False


ADJS, P, Q = parse_raw()

print(
    "yes" if exists_path(P, Q, ADJS)
    else "no" if exists_path(Q, P, ADJS)
    else "unknown"
)
