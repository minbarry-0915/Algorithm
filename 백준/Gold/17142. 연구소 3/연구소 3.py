import sys

# sys.stdin = open('input.txt', 'r', encoding='utf-8')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
from collections import deque

def bfs(active_virus):
    queue = deque()
    visited = [[-1] * n for _ in range(n)]
    for x, y in active_virus:
        queue.append((x, y))
        visited[x][y] = 0

    while queue:
        x,y = queue.popleft()

        for d in range(4):
            nx,ny = x + dx[d], y + dy[d]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1 and grid[nx][ny] != '1':
                queue.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1

    time = 0
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '0':
                if visited[i][j] == -1:
                    return int(1e9)
                time = max(time, visited[i][j])
    return time

n, m = map(int, input().split())
grid = [list(input().split()) for _ in range(n)]

virus_lst = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == '2':
            virus_lst.append((i, j))

from itertools import combinations

# m개씩 활성 바이러스 추출
cases = list(combinations(virus_lst, m))

answer = int(1e9)
for case in cases:
    result = bfs(case)
    answer = min(answer, result)

print(answer if answer != int(1e9) else -1)
