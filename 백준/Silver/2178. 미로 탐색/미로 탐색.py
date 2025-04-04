import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def is_valid(nx,ny):
    return 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not is_valid(nx, ny):
                continue

            grid[nx][ny] = grid[x][y] + 1
            queue.append((nx,ny))

    return grid[n - 1][m - 1]

print(bfs(0,0))
