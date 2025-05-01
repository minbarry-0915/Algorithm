from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = 100


def bfs(sx, sy, ex, ey, visited, grid):
    queue = deque()
    queue.append((sx, sy))
    visited[sx][sy] = True

    while queue:
        cx, cy = queue.popleft()
        if cx == ex and cy == ey:
            return 1

        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] != '1':
                queue.append((nx, ny))
                visited[nx][ny] = True

    return 0


for _ in range(10):
    t = int(input())
    grid = [input().strip() for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    start_x, start_y = 0, 0
    end_x, end_y = 0, 0

    for i in range(n):
        for j in range(n):
            if grid[i][j] == '2':
                start_x, start_y = i, j
            elif grid[i][j] == '3':
                end_x, end_y = i, j

    result = bfs(start_x, start_y, end_x, end_y, visited, grid)
    print(f'#{t} {result}')
