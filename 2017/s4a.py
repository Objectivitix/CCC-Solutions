# Naive O(M^2 log M) solution doesn't even pass
# M <= 5000 😔 But it still gets 11 points :D


class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def make(self, item):
        self.parent[item] = item
        self.size[item] = 1

    def find(self, item):
        root = item

        while self.parent[root] != root:
            root = self.parent[root]

        # Path compression seems to offer
        # only marginal benefits. Womp womp
        while self.parent[item] != item:
            item, self.parent[item] = self.parent[item], root

        return root

    def union(self, a, b):
        p, q = self.find(a), self.find(b)

        assert p != q

        if self.size[p] < self.size[q]:
            p, q = q, p

        self.parent[q] = p
        self.size[p] += self.size[q]


def sort(edges):
    return sorted(edges, key=lambda e: e[2])


def find_min_tree(nodes, sorted_edges):
    components = UnionFind()

    for node in nodes:
        components.make(node)

    tree = set()
    weight = 0

    for u, v, w in sorted_edges:
        if components.find(u) == components.find(v):
            continue

        tree.add((u, v))
        weight += w

        components.union(u, v)

    return tree, weight


def find_min_tree_with_adjustment(d, nodes, edges):
    if d == 0:
        return find_min_tree(nodes, sort(edges))

    _edges = edges.copy()

    min_tree = None
    min_weight = float("inf")

    for i, (u, v, w) in enumerate(_edges):
        _edges[i] = (u, v, max(0, w - d))

        tree, weight = find_min_tree(nodes, sort(_edges))

        if weight < min_weight:
            min_tree = tree
            min_weight = weight

        _edges[i] = (u, v, w)

    return min_tree, min_weight


def parse_raw():
    n, m, d = map(int, input().split())

    nodes = set()
    edges = []

    for _ in range(m):
        u, v, w = map(int, input().split())

        nodes.add(u)
        nodes.add(v)

        edges.append((u, v, w))

    return n, m, d, nodes, edges


N, M, D, NODES, EDGES = parse_raw()

current_tree = set((u, v) for u, v, _ in EDGES[:N - 1])
min_tree, _ = find_min_tree_with_adjustment(D, NODES, EDGES)

to_deactivate = current_tree - min_tree
to_activate = min_tree - current_tree

print(max(len(to_deactivate), len(to_activate)))
