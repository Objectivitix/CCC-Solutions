from collections import deque

n = int(input())

adj_list = {}
dist = {}

for page_num in range(1, n + 1):
    _, *pages_linked = map(int, input().split())
    adj_list[page_num] = pages_linked

    dist[page_num] = float("inf")

source = 1
dist[source] = 0
dq = deque([source])

while dq:
    curr_node = dq.popleft()

    for neighbor in adj_list[curr_node]:
        alt_dist = dist[curr_node] + 1

        if alt_dist < dist[neighbor]:
            dist[neighbor] = alt_dist
            dq.append(neighbor)

print("N" if float("inf") in dist.values() else "Y")
print(min(distance for node, distance in dist.items() if len(adj_list[node]) == 0) + 1)
