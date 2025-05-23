n = int(input())
m = int(input())
graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost))

start, end = map(int,input().split())

INF = int(1e9)
dist = [INF] * (n + 1)
dist[start] = 0

heap = []
import heapq
heapq.heappush(heap, (0, start)) # cost, v

while heap:
    cost, now = heapq.heappop(heap)

    if cost > dist[now]:
        continue
    for n_node, n_cost in graph[now]:
        new_cost = cost + n_cost
        if new_cost < dist[n_node]:
            dist[n_node] = new_cost
            heapq.heappush(heap, (new_cost, n_node))
print(dist[end])