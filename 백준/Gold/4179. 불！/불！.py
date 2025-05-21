dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]

# 지훈이 이동
# 불 퍼짐
# 시간 출력
from collections import deque

fire_q = deque()
user_q = deque()
visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if grid[i][j] == 'F':
            fire_q.append((i, j))
        elif grid[i][j] == 'J':
            user_q.append((i, j, 0))
            visited[i][j] = True


def spread_fire():
    for _ in range(len(fire_q)):
        x, y = fire_q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '.':
                grid[nx][ny] = 'F'
                fire_q.append((nx, ny))


def move():
    for _ in range(len(user_q)):
        x, y, time = user_q.popleft()

        if x == 0 or x == n - 1 or y == 0 or y == m - 1:
            print(time + 1)
            return True

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and grid[nx][ny] == '.':
                    visited[nx][ny] = True
                    user_q.append((nx, ny, time + 1))
    return False

while True:
    spread_fire()
    escaped = move()
    if escaped:
        break
    if not user_q:
        print("IMPOSSIBLE")
        break