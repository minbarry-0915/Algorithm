import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())

# 3차원 grid 입력
grid = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

# 상,하,좌,우,위,아래 방향
dx = [0, 0, -1, 1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

queue = deque()

# 익은 토마토 위치 큐에 삽입
for z in range(h):
    for y in range(n):
        for x in range(m):
            if grid[z][y][x] == 1:
                queue.append((z, y, x))

def bfs():
    while queue:
        z, y, x = queue.popleft()

        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m and grid[nz][ny][nx] == 0:
                grid[nz][ny][nx] = grid[z][y][x] + 1
                queue.append((nz, ny, nx))

bfs()

# 결과 계산
result = 0
for z in range(h):
    for y in range(n):
        for x in range(m):
            if grid[z][y][x] == 0:
                print(-1)
                sys.exit()
            result = max(result, grid[z][y][x])

print(result - 1)
