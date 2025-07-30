
from itertools import combinations
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(viruses):
    queue = deque()
    visited = [[-1] * n for _ in range(n)]
    for vx,vy in viruses:
        queue.append((vx,vy))
        visited[vx][vy] = 0

    while queue:
        x,y = queue.popleft()

        for d in range(4):
            nx,ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if grid[nx][ny] != 1:
                    queue.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1

    # 검증
    max_time = max([max(row) for row in visited])
    not_spread = False
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                continue
            if visited[i][j] == -1:
                not_spread = True
                break
        if not_spread:
            break
    return max_time, not_spread

n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]

virus_available_positions = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            virus_available_positions.append((i,j))

min_time = int(1e9)
for cases in combinations(virus_available_positions, m):
    time, not_spread = bfs(cases)
    if not not_spread:
        min_time = min(min_time, time)

if min_time == int(1e9):
    print(-1)
else:
    print(min_time)