from collections import deque
input = __import__('sys').stdin.readline
n = 8
graph = [list(input().strip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx = [0, 0, 1, -1, 1, -1, 1, -1, 0]
dy = [1, -1, 0, 0, 1, 1, -1, -1, 0]

q = deque()
q.append((7, 0))
visited[7][0] = True
ans = 0
while q:
    i, j = q.popleft()
    if graph[i][j] == '#':
        continue
    for idx in range(n + 1):
        ni = i + dy[idx]
        nj = j + dx[idx]
        if ni < 0 or ni >= n or nj < 0 or nj >= n or graph[ni][nj] == '#':
            continue
        if ni == 0:
            ans = 1
        if not visited[ni - 1][nj]:
            visited[ni - 1][nj] = True
            q.append((ni - 1, nj))
print(ans)