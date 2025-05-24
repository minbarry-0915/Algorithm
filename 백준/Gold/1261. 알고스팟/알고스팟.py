m, n = map(int, input().split())
grid = [list(input()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
from collections import deque

queue = deque()
visited = [[False] * m for _ in range(n)]
visited[0][0] = True
queue.append((0, 0, 0))

while queue:
    x, y, cnt = queue.popleft()
    if x == n - 1 and y == m - 1:
        print(cnt)
        break

    for d in range(4):
        nx,ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            if grid[nx][ny] == "1":
                queue.append((nx,ny,cnt + 1))
            elif grid[nx][ny] == '0':
                queue.appendleft((nx,ny,cnt))
