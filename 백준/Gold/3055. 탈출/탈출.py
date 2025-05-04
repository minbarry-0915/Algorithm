import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n,m = map(int,input().split())
grid = []
water_time = [[-1] * m for _ in range(n)]
hedgedog_time = [[-1] * m for _ in range(n)]
w_queue = deque()
h_queue = deque()

for i in range(n):
    row = list(input().strip())
    grid.append(row)
    for j in range(m):
        if row[j] == '*':
            water_time[i][j] = 0
            w_queue.append((i,j))
        elif row[j] == 'S':
            start_x, start_y = i,j
            hedgedog_time[i][j] = 0
            h_queue.append((i,j))
        elif row[j] == 'D':
            end_x, end_y = i,j


# 물 이동 계산
while w_queue:
    x,y = w_queue.popleft()
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m:
            if grid[nx][ny] == '.' and water_time[nx][ny] == -1:
                water_time[nx][ny] = water_time[x][y] + 1
                w_queue.append((nx,ny))
# 고슴도치 이동
while h_queue:
    x,y = h_queue.popleft()
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <=  nx < n and 0 <= ny < m:
            if hedgedog_time[nx][ny] == -1:
                if grid[nx][ny] == 'D':
                    print(hedgedog_time[x][y] + 1)
                    exit(0)
                if grid[nx][ny] == '.':
                    if water_time[nx][ny] == -1 or hedgedog_time[x][y] + 1 < water_time[nx][ny]:
                        hedgedog_time[nx][ny] = hedgedog_time[x][y] + 1
                        h_queue.append((nx,ny))
print('KAKTUS')