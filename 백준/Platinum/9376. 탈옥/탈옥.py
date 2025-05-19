import sys

# sys.stdin = open('input.txt', 'r', encoding='UTF-8')
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, grid):
    visited = [[-1] * (m + 2) for _ in range(n + 2)]
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 0
    while queue:
        cx, cy = queue.popleft()
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < n + 2 and 0 <= ny < m + 2 and grid[nx][ny] != '*' and visited[nx][ny] == -1:
                if grid[nx][ny] == '.' or grid[nx][ny] == '$':
                    visited[nx][ny] = visited[cx][cy]
                    queue.appendleft((nx,ny))
                elif grid[nx][ny] == '#':
                    visited[nx][ny] = visited[cx][cy] + 1
                    queue.append((nx,ny))

    return visited
T = int(input())
for t in range(1, T + 1):
    n, m = map(int, input().split())
    grid = []
    grid.append(['.'] * (m + 2))
    for _ in range(n):
        grid.append(list('.' + input().strip() + '.'))
    grid.append(['.'] * (m + 2))
    prisoner = []
    for i in range(n + 2):
        for j in range(m + 2):
            if grid[i][j] == '$':
                prisoner.append((i, j))

    visited_1 = bfs(prisoner[0][0], prisoner[0][1], grid)
    visited_2 = bfs(prisoner[1][0], prisoner[1][1], grid)
    visited_3 = bfs(0, 0, grid)
    ans = int(1e9)
    for i in range(n + 2):
        for j in range(m + 2):
            if visited_1[i][j] == -1 or visited_2[i][j] == -1 or visited_3[i][j] == -1:
                continue
            total = visited_1[i][j] + visited_2[i][j] + visited_3[i][j]
            if grid[i][j] == '#':
                total -= 2
            ans = min(total, ans)
    print(ans)