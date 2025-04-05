import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def melt():
    temp = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0:
                sea = 0
                for k in range(4):
                    ni, nj = i + dx[k], j + dy[k]
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 0: #바다랑 인접
                        sea += 1
                temp[i][j] = max(grid[i][j] - sea, 0) #녹은거 임시에 저장

   # grid에 녹은거 반영
    return temp


def bfs(x,y,visited):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] > 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))


year = 0
while True:
    count = 0
    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0 and not visited[i][j]:
                bfs(i,j,visited)
                count += 1

    if count == 0:
        print(0)
        break
    if count >= 2:
        print(year)
        break

    grid = melt()
    year += 1