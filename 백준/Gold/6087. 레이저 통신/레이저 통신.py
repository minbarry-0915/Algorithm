#import sys
from collections import deque

#sys.stdin = open('input.txt', 'r', encoding='utf-8')

dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]


def bfs(i, j):
    visited = [[[float('inf')] * 4 for _ in range(m)] for _ in range(n)]
    queue = deque()

    for d in range(4):
        visited[i][j][d] = 0
        queue.append((i, j, d))

    while queue:
        x, y, cd = queue.popleft()

        nx = x + dx[cd]
        ny = y + dy[cd]

        while 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != '*':
            # 같은 방향으로 이동
            if visited[nx][ny][cd] > visited[x][y][cd]:
                visited[nx][ny][cd] = visited[x][y][cd]
                queue.append((nx, ny, cd))

            # 방향 바꿔 거울 설치
            for nd in range(4):
                if nd != cd:
                    if visited[nx][ny][nd] > visited[x][y][cd] + 1:
                        visited[nx][ny][nd] = visited[x][y][cd] + 1
                        queue.append((nx, ny, nd))

            nx += dx[cd]
            ny += dy[cd]

    return min(visited[end[0]][end[1]])


# 입력 처리
m, n = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

c_points = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'C':
            c_points.append((i, j))

start = c_points[0]
end = c_points[1]

# 시작과 끝이 같을 경우
if start == end:
    print(0)
else:
    print(bfs(start[0], start[1]))
