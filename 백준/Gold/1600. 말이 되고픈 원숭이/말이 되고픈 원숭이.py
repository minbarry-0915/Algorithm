import sys
from collections import deque

# sys.stdin = open('input.txt','r')
# 입력
k = int(sys.stdin.readline())
w, h = map(int, sys.stdin.readline().split())
grid = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]

# 방향 벡터
# 일반 이동 (상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 말 이동 (체스의 나이트)
hx = [-2, -1, 1, 2, 2, 1, -1, -2]
hy = [1, 2, 2, 1, -1, -2, -2, -1]

# visited[x][y][말 점프 횟수] = 이동 횟수
visited = [[[-1] * (k + 1) for _ in range(w)] for _ in range(h)]


def bfs():
    queue = deque()
    queue.append((0, 0, 0))  # (x, y, 말 점프 횟수)
    visited[0][0][0] = 0  # 시작 지점도 이동 횟수로 카운트

    while queue:
        x, y, horse = queue.popleft()

        # 도착
        if x == h - 1 and y == w - 1:
            return visited[x][y][horse]

        # 일반 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if grid[nx][ny] == 0 and visited[nx][ny][horse] == -1:
                    visited[nx][ny][horse] = visited[x][y][horse] + 1
                    queue.append((nx, ny, horse))

        # 말 이동
        if horse < k:
            for i in range(8):
                nx = x + hx[i]
                ny = y + hy[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if grid[nx][ny] == 0 and visited[nx][ny][horse + 1] == -1:
                        visited[nx][ny][horse + 1] = visited[x][y][horse] + 1
                        queue.append((nx, ny, horse + 1))

    return -1


print(bfs())
