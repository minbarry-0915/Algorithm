from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(n, m, grid, visited):
    queue = deque([(0, 0)])
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if grid[nx][ny] == 0 or grid[nx][ny] == 2:
                    visited[nx][ny] = True
                    grid[nx][ny] = 2
                    queue.append((nx, ny))

def melt_cheese(n,m,grid):
    melted = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                count = 0
                for d in range(4):
                    nx, ny = i + dx[d], j + dy[d]
                    if 0 <= nx < n and 0 <= ny < m:
                        if grid[nx][ny] == 2:
                            count += 1
                if count >= 2:
                    melted.append((i,j))
    for x, y in melted:
        grid[x][y] = 0
    return len(melted)


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
time = 0
while True:
    # 외부 공기 처리
    visited = [[False] * m for _ in range(n)]
    bfs(n, m, grid, visited)
    melted = melt_cheese(n, m, grid)

    if melted == 0:
        break
    time += 1
print(time)