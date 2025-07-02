n = int(input())
m = int(input())
routes = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    a,b,c = map(int,input().split())
    routes[a].append((b,c))
start,end = map(int,input().split())

import heapq
heap = []
heapq.heappush(heap, (0,start))
costs = [int(1e9)] * (n + 1)
costs[start] = 0
prev = [0] * (n + 1)
while heap:
    curr_cost, curr_node = heapq.heappop(heap)

    if costs[curr_node] < curr_cost:
        continue

    for next_node, cost in routes[curr_node]:
        next_cost = curr_cost + cost
        if costs[next_node] > next_cost:
            costs[next_node] = next_cost
            prev[next_node] = curr_node
            heapq.heappush(heap, (next_cost, next_node))

path = []
node = end
while node != 0:
    path.append(node)
    node = prev[node]
path.reverse()

print(costs[end])
print(len(path))
print(* path)