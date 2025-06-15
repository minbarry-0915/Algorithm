import sys
from collections import deque

# sys.stdin = open('input.txt','r')

dx = [-1,1,0,0]
dy = [0,0,-1,1]

T = int(input())
for tc in range(1, T + 1):
    m,n = map(int,input().split())
    grid = []
    user_x, user_y = 0,0
    fire_queue = []

    grid.append(['x'] * (m + 2))

    for _ in range(n):
        line = list(input().strip())
        grid.append(['x'] + line + ['x'])

    grid.append(['x'] * (m + 2))


    fire_queue = deque()
    fire_time = [[-1] * (m + 2) for _ in range(n + 2)]

    user_queue = deque()
    user_time = [[-1] * (m + 2) for _ in range(n + 2)]

    # 초기 위치 탐색
    for i in range(n + 2):
        for j in range(m + 2):
            if grid[i][j] == '*':
                fire_queue.append((i, j))
                fire_time[i][j] = 0
            elif grid[i][j] == '@':
                user_queue.append((i, j))
                user_time[i][j] = 0

    while fire_queue:
        x,y = fire_queue.popleft()
        for d in range(4):
            nx,ny = x + dx[d], y + dy[d]
            if grid[nx][ny] in ['.','@'] and fire_time[nx][ny] == -1:
                fire_time[nx][ny] = fire_time[x][y] + 1
                fire_queue.append((nx,ny))

    escaped = False
    while user_queue:
        x,y = user_queue.popleft()

        if grid[x][y] == 'x':
            print(user_time[x][y])
            escaped = True

            break

        for d in range(4):
            nx,ny = x + dx[d], y + dy[d]

            if grid[nx][ny] in ['.','x'] and user_time[nx][ny] == -1:
                arrive_time = user_time[x][y] + 1
                if fire_time[nx][ny] == -1 or arrive_time < fire_time[nx][ny]:
                    user_time[nx][ny] = arrive_time
                    user_queue.append((nx,ny))

    if not escaped:
        print('IMPOSSIBLE')


