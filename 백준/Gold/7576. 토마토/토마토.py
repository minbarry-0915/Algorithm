import sys
from collections import deque

#sys.stdin = open('input.txt', 'r')
m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()

# 익은 토마토 처음에 전부 큐에 넣기
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            queue.append((i, j))

while queue:
    x, y = queue.popleft()
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if grid[nx][ny] == 0:
                grid[nx][ny] = grid[x][y] + 1
                queue.append((nx, ny))

# 결과 확인
result = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:  # 안 익은 토마토가 있음
            print(-1)
            sys.exit()
        result = max(result, grid[i][j])

print(result - 1)  # 처음 익은 토마토가 1이었으므로 -1
