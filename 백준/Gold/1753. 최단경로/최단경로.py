v,e = map(int,input().split())
k = int(input())

graph = {i: [] for i in range(1,v+1)}
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

import heapq

INF = float('inf')
dijkstra = [INF] * (v + 1)
dijkstra[k] = 0
heap = []
heapq.heappush(heap, (0,k))
while heap:
    cur_cost, cur_node  = heapq.heappop(heap)

    if dijkstra[cur_node] < cur_cost:
        continue

    for node,cost in graph[cur_node]:
        new_cost = cur_cost + cost
        if dijkstra[node] > new_cost:
            dijkstra[node] = new_cost
            heapq.heappush(heap, (new_cost, node))

for i in range(1, v + 1):
    print(dijkstra[i] if dijkstra[i] != INF else 'INF')