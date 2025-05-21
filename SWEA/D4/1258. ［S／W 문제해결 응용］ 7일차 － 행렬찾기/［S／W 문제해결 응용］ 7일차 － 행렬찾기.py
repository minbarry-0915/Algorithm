dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
from collections import deque


def bfs(x, y, visited, matrix):
    visited[x][y] = True
    queue = deque()
    queue.append((x, y))
    route = []
    while queue:
        cx, cy = queue.popleft()
        route.append((cx, cy))
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and matrix[nx][ny] != 0:
                visited[nx][ny] = True
                queue.append((nx, ny))
    xs = [c[0] for c in route]
    ys = [c[1] for c in route]
    row = max(xs) - min(xs) + 1
    col = max(ys) - min(ys) + 1
    return row, col


T = int(input())

for t in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    submatrix_lst = []
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0 and not visited[i][j]:
                row, col = bfs(i, j, visited, matrix)
                submatrix_lst.append((row, col))

    print(f'#{t} {len(submatrix_lst)}', end=' ')

    submatrix_lst.sort(key=lambda x: (x[0] * x[1], x[0]))
    for r, c in submatrix_lst:
        print(r, c, end=' ')
    print()
