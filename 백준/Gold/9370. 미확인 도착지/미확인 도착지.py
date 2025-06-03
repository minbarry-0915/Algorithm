import sys

# sys.stdin = open('input.txt', 'r', encoding='utf-8')
import heapq


def dijkstra(start, graph, n):
    INF = int(1e9)
    distance = [INF] * (n + 1)
    distance[start] = 0
    heap = [(0,start)]

    while heap:
        dist, now = heapq.heappop(heap)
        if distance[now] < dist:
            continue
        for next, cost in graph[now]:
            total_cost = dist + cost
            # 더 좋은 경로 발견
            if total_cost < distance[next]:
                distance[next] = total_cost
                heapq.heappush(heap, (total_cost, next))
    return distance

T = int(input())
for tc in range(1, T + 1):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = {i: [] for i in range(1, n + 1)}
    for _ in range(m):
        a,b,d = map(int,input().split())
        graph[a].append((b,d))
        graph[b].append((a,d))
    candidates = [int(input()) for _ in range(t)]

    dist_s = dijkstra(s,graph, n) # 시작 지점부터 모든 지점까지의 최단 경로 탐색
    dist_g = dijkstra(g,graph, n)
    dist_h = dijkstra(h,graph, n)

    result = []
    for x in candidates:
        path1 = dist_s[g] + dist_g[h] + dist_h[x]
        path2 = dist_s[h] + dist_h[g] + dist_g[x]
        if dist_s[x] == min(path1, path2):
            result.append(x)
    result.sort()
    print(* result)