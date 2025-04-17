
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(target, i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 1
    count = 1

    while queue:
        cx, cy = queue.popleft()

        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == target:
                visited[nx][ny] = 1
                count += 1
                queue.append((nx, ny))

    return count


m, n = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

visited = [[0] * m for _ in range(n)]
W_power = 0
B_power = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if grid[i][j] == 'W':
                count = bfs('W', i, j)
                W_power += count ** 2
            else:
                count = bfs('B', i, j)
                B_power += count ** 2
print(W_power, B_power)
