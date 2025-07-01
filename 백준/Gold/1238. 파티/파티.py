
INF = int(1e9)
n,m,x = map(int,input().split())
graph = {i: [] for i in range(1, n + 1)}
reverse_graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    reverse_graph[b].append((a, c))   # 반대 방향

'''
접근
각학생이 x로 이동해야됨
-> x기준 각학생에게 가는 최소 비용 계산 + 학생에서 x에게 가는 최소비용 계산
-> 비용 계산 한것 중 최솟값 추출
'''

# 초기화
import heapq

def dijkstra(start, g):
    distance = [INF] * (n + 1)
    distance[start] = 0
    heap = [(0, start)]

    while heap:
        dist, node = heapq.heappop(heap)

        if distance[node] < dist:
            continue

        for neighbor, cost in g[node]:
            new_cost = dist + cost
            if new_cost < distance[neighbor]:
                distance[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))
    return distance

# x → i
go = dijkstra(x, graph)
# i → x
back = dijkstra(x, reverse_graph)

# 왕복 거리의 최댓값
result = 0
for i in range(1, n + 1):
    total = go[i] + back[i]
    result = max(result, total)

print(result)