# Low-level constant optimisation is not a test of
# programming fluency, much less algorithmic
# thinking. But alas, I chose to code in Python, so
# I guess these are the consequences :P
#
# Things learned from this (very surprisingly easy)
# problem: 1) sys can provide fast I/O; 2) ints are
# faster than one-char strings.

import sys
from collections import defaultdict, deque

input = sys.stdin.readline


def parse_raw():
    _, m = map(int, input().split())

    adj_list = defaultdict(list)

    for _ in range(m):
        u, v = map(int, input().split())
        adj_list[u].append(v)

    p, q = map(int, input().split())

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
