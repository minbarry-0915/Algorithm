# 이동 방향 (상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 입력
n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]


# 빙하 녹음
# 백조 이동 시도
# 시간 출력
def move_swans():
    while swan_q:
        x, y = swan_q.popleft()

        if grid[x][y] == 'L' and x == swans[1][0] and y == swans[1][1]:
            return True

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                if grid[nx][ny] == '.' or grid[nx][ny] == 'L':
                    swan_q.append((nx, ny))
                elif grid[nx][ny] == 'X':
                    next_swan_q.append((nx, ny))
    return False


def melt_ice():
    while water_q:
        x, y = water_q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == 'X':
                    grid[nx][ny] = '.'
                    next_water_q.append((nx, ny))


from collections import deque

swans = []
water_q = deque()
next_water_q = deque()
visited = [[False] * m for _ in range(n)]

swan_q = deque()
next_swan_q = deque()

for i in range(n):
    for j in range(m):
        if grid[i][j] != 'X':  # 물 or 백조
            water_q.append((i, j))
        if grid[i][j] == 'L':
            swans.append((i, j))

swan_q.append(swans[0])  # x,y
visited[swans[0][0]][swans[0][1]] = True

day = 0
while True:
    if move_swans():
        print(day)
        break
    melt_ice()
    water_q = next_water_q
    swan_q = next_swan_q
    next_water_q = deque()
    next_swan_q = deque()
    day += 1
