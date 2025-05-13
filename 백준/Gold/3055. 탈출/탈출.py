from collections import deque
import sys

# sys.stdin = open('input.txt', 'r', encoding='utf-8')
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

water_q = deque()
go_q = deque()
visited = [[False]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if grid[i][j] == 'S':
            go_q.append((i, j, 0))
            visited[i][j] = True
        elif grid[i][j] == '*':
            water_q.append((i, j))

def spread_water():
    for _ in range(len(water_q)):
        x, y = water_q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == '.':
                    grid[nx][ny] = '*'
                    water_q.append((nx, ny))

def move_go():
    for _ in range(len(go_q)):
        x, y, time = go_q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == 'D':
                    print(time + 1)
                    exit()
                if grid[nx][ny] == '.' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    go_q.append((nx, ny, time + 1))

while go_q:
    spread_water()
    move_go()

print("KAKTUS")
