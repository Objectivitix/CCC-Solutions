import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100001)


def parse_raw():
    n, m = map(int, input().split())

    yield n
    yield m

    yield set(input().split())

    adj_list = defaultdict(list)

    for _ in range(n - 1):
        a, b = input().split()
        adj_list[a].append(b)
        adj_list[b].append(a)

    yield adj_list


def get_leaves(adj_list):
    for node in adj_list:
        if len(adj_list[node]) == 1:
            yield node


def prune(adj_list, include):
    valid = {}
    visited = set()
    leaves = set(get_leaves(adj_list))

    def dfs(curr):
        visited.add(curr)

        sub_valid = []

        for adj in adj_list[curr]:
            if adj not in visited:
                dfs(adj)
                sub_valid.append(valid[adj])

        valid[curr] = any(sub_valid) or curr in include

    root = next(iter(include))
    dfs(root)

    return {node for node, flag in valid.items() if flag}


def pick(adj_list, nodes):
    subgraph = defaultdict(list)

    for node in adj_list:
        if node not in nodes:
            continue

        for adj in adj_list[node]:
            if adj not in nodes:
                continue

            subgraph[node].append(adj)

    return subgraph


def find_farthest_node(source, adj_list):
    dist = {source: 0}
    dq = deque([source])

    while dq:
        curr = dq.popleft()

        for adj in adj_list[curr]:
            alt_dist = dist[curr] + 1

            if alt_dist < dist.get(adj, float("inf")):
                dist[adj] = alt_dist
                dq.append(adj)

    return max(dist.items(), key=lambda entry: entry[1])


def find_diameter(adj_list):
    arbitrary_start = next(iter(adj_list))

    u, _ = find_farthest_node(arbitrary_start, adj_list)
    _, diameter = find_farthest_node(u, adj_list)

    return diameter


_, _, TARGETS, ADJ_LIST = parse_raw()

subgraph = pick(ADJ_LIST, prune(ADJ_LIST, TARGETS))
edges_n = len(subgraph) - 1
diameter = find_diameter(subgraph)

print(edges_n * 2 - diameter)
