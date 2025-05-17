import sys

# sys.stdin = open('input.txt', 'r', encoding='UTF-8')

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

from collections import deque

cheese_q = deque()
next_cheese_q = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs_air():
    visited = [[0] * m for _ in range(n)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if grid[nx][ny] == 0:
                    q.append((nx, ny))
                elif grid[nx][ny] == 1:
                    # 외부 공기와 닿은 치즈는 2로 표기
                    grid[nx][ny] = 2
                visited[nx][ny] = 1


def melt_cheese():
    melted = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                grid[i][j] = 0
                melted += 1
    return melted

time = 0
last_cheese = 0

while True:
    bfs_air()
    melted = melt_cheese()
    if melted == 0:
        break
    else:
        last_cheese = melted
        time += 1

print(time)
print(last_cheese)