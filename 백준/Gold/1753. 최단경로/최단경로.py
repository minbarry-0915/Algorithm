import sys
import heapq

# sys.stdin = open('input.txt', 'r')  # 채점 시 주석
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())
graph = {i: [] for i in range(1, v + 1)}

for _ in range(e):
    u, v_, cost = map(int, input().split())
    graph[u].append((v_, cost))

# 다익스트라
INF = int(1e9)
distance = [INF] * (v + 1)
distance[k] = 0
heap = [(0, k)]  # (비용, 정점)

while heap:
    dist, now = heapq.heappop(heap)

    if distance[now] < dist:
        continue

    for next_node, cost in graph[now]:
        next_dist = dist + cost
        if next_dist < distance[next_node]:
            distance[next_node] = next_dist
            heapq.heappush(heap, (next_dist, next_node))

for i in range(1, v + 1):
    print(distance[i] if distance[i] != INF else "INF")