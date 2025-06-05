import sys

# sys.stdin = open('input.txt', 'r', encoding='utf-8')

n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v, c = map(int, input().split())
    edges.append((u, v, c))

INF = int(1e9)
dist = [INF] * (n + 1)
dist[1] = 0  # 1번 노드 시작

# 거리 갱신 n-1번
for i in range(n - 1):
    for u, v, c in edges:
        if dist[u] != INF and dist[u] + c < dist[v]:
            dist[v] = dist[u] + c

# 음수 사이클 검사 (n번째 루프)
for u, v, c in edges:
    if dist[u] != INF and dist[u] + c < dist[v]:
        print(-1)
        sys.exit()

# 출력
for i in range(2, n + 1):
    print(dist[i] if dist[i] != INF else -1)