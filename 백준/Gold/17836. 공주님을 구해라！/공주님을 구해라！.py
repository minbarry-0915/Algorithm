import sys
from collections import deque

# sys.stdin = open('input.txt','r', encoding='utf-8')
input = sys.stdin.readline

n, m, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# visited[x][y][0]: 검 없음, [x][y][1]: 검 있음
visited = [[[-1]*2 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque()
queue.append((0, 0, 0))  # x, y, has_sword (0 or 1)
visited[0][0][0] = 0

while queue:
    x, y, sword = queue.popleft()

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            # 이미 방문했으면 pass
            if visited[nx][ny][sword] != -1:
                continue

            cell = grid[nx][ny]

            if cell == 0:
                visited[nx][ny][sword] = visited[x][y][sword] + 1
                queue.append((nx, ny, sword))

            elif cell == 1 and sword == 1:
                visited[nx][ny][sword] = visited[x][y][sword] + 1
                queue.append((nx, ny, sword))

            elif cell == 2:
                visited[nx][ny][1] = visited[x][y][sword] + 1
                queue.append((nx, ny, 1))

# 두 가지 경우 모두 확인
res1 = visited[n-1][m-1][0]
res2 = visited[n-1][m-1][1]

min_time = float('inf')
if res1 != -1:
    min_time = min(min_time, res1)
if res2 != -1:
    min_time = min(min_time, res2)

if min_time <= t:
    print(min_time)
else:
    print("Fail")
