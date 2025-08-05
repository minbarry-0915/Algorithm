
from collections import deque



n = int(input())
m = int(input())

INF = int(1e9)
dist = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dist[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    dist[a][b] = 1
    dist[b][a] = 1

# Floyd-Warshall
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][k] + dist[k][j] < dist[i][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

# 그룹 찾기 (BFS)
visited = [False] * (n + 1)
groups = []

for i in range(1, n + 1):
    if not visited[i]:
        group = []
        queue = deque([i])
        visited[i] = True

        while queue:
            cur = queue.popleft()
            group.append(cur)

            for j in range(1, n + 1):
                if dist[cur][j] != INF and not visited[j]:
                    visited[j] = True
                    queue.append(j)

        groups.append(group)

# 대표자 선정
representatives = []
for group in groups:
    min_score = INF
    rep = -1

    for person in group:
        score = max(dist[person][other] for other in group)

        if score < min_score:
            min_score = score
            rep = person

    representatives.append(rep)

# 대표자 정렬 및 출력
representatives.sort()

print(len(representatives))
for rep in representatives:
    print(rep)
