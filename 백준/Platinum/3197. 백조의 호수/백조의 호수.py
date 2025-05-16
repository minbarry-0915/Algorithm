import sys

# sys.stdin = open('input.txt', 'r', encoding='UTF-8')

input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

water_q = deque()
next_water_q = deque()

swans = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == '.' or grid[i][j] == 'L':
            water_q.append((i, j))
            if grid[i][j] == 'L':
                swans.append((i, j))

days = 0
swan_q = deque()
next_swan_q = deque() # 얼음 옆에 멈춰선 백조 (내일 이동 시도)
visited = [[False] * m for _ in range(n)]
swan_q.append(swans[0])
visited[swans[0][0]][swans[0][1]] = True


def melt():
    while water_q:
        x, y = water_q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == 'X':
                    grid[nx][ny] = '.' # 바꿔줘야 백조가 다음날 이동이 가능
                    next_water_q.append((nx, ny))


def move_swan():
    while swan_q:
        x, y = swan_q.popleft()
        if x == swans[1][0] and y == swans[1][1]:
            return True
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                if grid[nx][ny] == '.' or grid[nx][ny] == 'L':
                    swan_q.append((nx, ny))
                elif grid[nx][ny] == 'X':
                    next_swan_q.append((nx, ny))
    return False

while True:
    if move_swan():
        print(days)
        break
    melt()
    swan_q, next_swan_q = next_swan_q, deque()
    water_q, next_water_q = next_water_q, deque()
    days += 1
