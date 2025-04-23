import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
from collections import deque


def move(x, y, dx, dy, grid):
    count = 0
    while grid[x + dx][y + dy] != '#' and grid[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x, y, count


def bfs():
    while queue:
        rx, ry, bx, by, depth = queue.popleft()

        if depth >= 10:
            return -1

        for d in range(4):
            nrx, nry, rc = move(rx, ry, dx[d], dy[d], grid)
            nbx, nby, bc = move(bx, by, dx[d], dy[d], grid)
            if grid[nbx][nby] == 'O':
                continue

            if grid[nrx][nry] == 'O':
                return depth + 1

            if nrx == nbx and nry == nby:
                if rc > bc:
                    nrx -= dx[d]
                    nry -= dy[d]
                else:
                    nbx -= dx[d]
                    nby -= dy[d]

            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                queue.append((nrx, nry, nbx, nby, depth + 1))
    return -1

n, m = map(int, input().split())
grid = [input() for _ in range(n)]
rx, ry = 0, 0
bx, by = 0, 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'R':
            rx, ry = i, j
        elif grid[i][j] == 'B':
            bx, by = i, j
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

queue = deque()
queue.append((rx, ry, bx, by, 0))
visited[rx][ry][bx][by] = True
print(bfs())
