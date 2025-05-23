from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(grid, end_x, end_y):
    queue = deque()
    queue.append((1, 1))
    visited = [[False] * 16 for _ in range(16)]
    visited[1][1] = True

    while queue:
        x,y = queue.popleft()
        if x == end_x and y == end_y:
            return True
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < 16 and 0 <= ny < 16 and not visited[nx][ny] and grid[nx][ny] != '1':
                queue.append((nx,ny))
                visited[nx][ny] = True

    return False

for _ in range(10):
    t = int(input())
    grid = [list(input()) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if grid[i][j] == '3':
                end_x, end_y = i, j
    print(f'#{t}', end=' ')
    print(1 if bfs(grid, end_x, end_y) else 0)
