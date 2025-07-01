
n,e = map(int,input().split())
graph = {i: [] for i in range(1,n + 1)}
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

v1 ,v2 = map(int,input().split())

import heapq
def dijkstra(start):
    heap = []
    dist = [int(1e9)] * (n + 1)
    heapq.heappush(heap, (0,start))
    dist[start] = 0

    while heap:
        curr_cost, curr_node = heapq.heappop(heap)

        if dist[curr_node] < curr_cost:
            continue

        for next, cost in graph[curr_node]:
            next_cost = curr_cost + cost
            if dist[next] > next_cost:
                dist[next] = next_cost
                heapq.heappush(heap, (next_cost, next))
    return dist

'''
접근
1번에 모든 경로로 가는 최소비용
v1에서 모든 경로로 가는 최소비용
v2에서 모든 경로로 가는 최소비용
셋을 더하면 두 정점을 거치는 최소비용이 나옴

1->v1->v2->n
1->v2->v1->n
'''

d1 = dijkstra(1)
dv1 = dijkstra(v1)
dv2 = dijkstra(v2)

route_1 = d1[v1] + dv1[v2] + dv2[n]
route_2 = d1[v2] + dv2[v1] + dv1[n]
result = min(route_1, route_2)
print(result if result < int(1e9) else -1)