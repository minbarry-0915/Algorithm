
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(i,j):
    visited[i][j] = 1
    queue = deque()
    queue.append((i,j))
    count = 1
    while queue:
        cx,cy = queue.popleft()

        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and grid[nx][ny]:
                    visited[nx][ny] = 1
                    count += 1
                    queue.append((nx,ny))
    return count


n, m, k = map(int, input().split())
grid = [[0] * m for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    grid[x - 1][y - 1] = 1

visited = [[0] * m for _ in range(n)]
max_cnt = -1
for i in range(n):
    for j in range(m):
        if not visited[i][j] and grid[i][j] == 1:
            count = bfs(i,j)
            max_cnt = max(max_cnt, count)

print(max_cnt)