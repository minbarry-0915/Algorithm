from collections import deque

def solution(n):
    # 동남서북
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    visited = [[0] * n for _ in range(n)]

    x, y, d = 0, 0, 0
    num = 1
    visited[x][y] = num

    while num < n * n:
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
            num += 1
            visited[nx][ny] = num
            x, y = nx, ny
        else:
            d = (d + 1) % 4  # 방향 전환

    return visited
