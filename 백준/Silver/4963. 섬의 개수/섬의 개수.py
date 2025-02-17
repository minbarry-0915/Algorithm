import sys

sys.setrecursionlimit(10 ** 6)  # 재귀 제한 증가
input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]


def dfs(x, y, w, h):
    visited[x][y] = True

    for i in range(8):  # 8방향 탐색
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] == 1:
            dfs(nx, ny, w, h)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break  # 입력 종료 조건

    grid = [list(map(int, input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    count = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and not visited[i][j]:  # 섬 발견
                count += 1
                dfs(i, j, w, h)

    print(count)
