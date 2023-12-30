# Full points O(N) solution.
#
# Finding the smallest subtree G containing all
# targets is key. Notice that all leaves of G must
# be targets. Say the problem was different, and
# we had to return to our starting restaurant. We
# must then travel through each edge twice.
#
# But we don't have this restraint. We want to
# minimize the total path length, so we want to
# maximize the path whose constituent edges we'll
# only visit once each. This is the diameter of G.
#
# All that's left to do is figuring out the first
# step: pruning the original tree down to G. We do
# this by rooting the tree, then traversing depth-
# first, tracking which nodes must be members of G.

import sys
from collections import defaultdict, deque

sys.setrecursionlimit(100_000)


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


def prune(adj_list, include):
    valid = {}
    visited = set()

    def traverse(curr):
        visited.add(curr)

        valid_in_subtree = False

        for adj in adj_list[curr]:
            if adj in visited:
                continue

            traverse(adj)

            if valid[adj]:
                valid_in_subtree = True

        valid[curr] = curr in include or valid_in_subtree

    # We must root the tree at one of the targets.
    root = next(iter(include))
    traverse(root)

    return {
        u: [v for v in adj_list[u] if valid[v]]
        for u in adj_list if valid[u]
    }


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

pruned = prune(ADJ_LIST, TARGETS)
edges_n = len(pruned) - 1
diameter = find_diameter(pruned)

print(edges_n * 2 - diameter)
