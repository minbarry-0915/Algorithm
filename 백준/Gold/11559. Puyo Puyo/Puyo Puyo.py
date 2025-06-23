
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n = 12
m = 6
grid = [list(input()) for _ in range(n)]

from collections import deque


def bfs(x, y, color):
    q = deque()
    q.append((x, y))
    visited = [[False] * m for _ in range(n)]
    visited[x][y] = True
    route = set([])
    route.add((x, y))

    while q:
        cx, cy = q.popleft()
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == color:
                visited[nx][ny] = True
                route.add((nx, ny))
                q.append((nx, ny))
    return len(route), route


def drop():
    # 열단위로 긁어서 재갱신
    for col in range(m):
        stack = []
        for row in range(n - 1, -1, -1):
            if grid[row][col] != '.':
                stack.append(grid[row][col])
        for row in range(n - 1, -1, -1):
            if stack:
                grid[row][col] = stack.pop(0)
            else:
                grid[row][col] = '.'

turn = 0
while True:
    popped = False
    for i in range(n):
        for j in range(m):
            if grid[i][j] in ['R', 'G', 'B', 'P', 'Y']:
                count, route = bfs(i, j, grid[i][j])
                if count >= 4:
                    popped = True
                    for x, y in route:
                        grid[x][y] = '.'

    if not popped:  # 내릴게 없음
        break

    drop()
    turn += 1
print(turn)
