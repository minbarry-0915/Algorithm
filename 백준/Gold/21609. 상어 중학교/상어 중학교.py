import sys
from collections import deque
# sys.stdin = open('input.txt','r')
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
# -1: 검은블록, 0: 무지개, 1..m: 일반블록, -2: 제거되어 빈칸

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(sx, sy, visited):
    color = grid[sx][sy]
    if color <= 0:  # 일반 블록(>0)에서만 시작
        return -1, -1, -1, -1, []

    q = deque([(sx, sy)])
    local_visited = [[False]*n for _ in range(n)]
    local_visited[sx][sy] = True
    route = [(sx, sy)]
    rainbow_count = 0

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and not local_visited[nx][ny]:
                if grid[nx][ny] == color or grid[nx][ny] == 0:
                    local_visited[nx][ny] = True
                    q.append((nx, ny))
                    route.append((nx, ny))
                    if grid[nx][ny] == 0:
                        rainbow_count += 1

    if len(route) < 2:
        return -1, -1, -1, -1, []

    # 전역 visited에는 무지개(0)를 제외한 일반 블록만 표시
    for x, y in route:
        if grid[x][y] != 0:
            visited[x][y] = True

    # 기준 블록: 무지개가 아닌 블록들 중 (행,열) 값이 가장 작은 것 (우선 행)
    normals = [(x, y) for (x, y) in route if grid[x][y] != 0]
    base_row, base_col = min(normals)  # tuple 비교로 (row 우선, col 다음)
    return len(route), rainbow_count, base_row, base_col, route

def gravity():
    # 각 열마다 위->아래가 아니라 아래에서 위로 내려보는 방식
    for j in range(n):
        for i in range(n-2, -1, -1):  # 아래에서 위로
            if grid[i][j] >= 0:  # 블록(일반 또는 무지개)
                x = i
                while x + 1 < n and grid[x+1][j] == -2:
                    grid[x+1][j] = grid[x][j]
                    grid[x][j] = -2
                    x += 1

def rotate_90_counter():
    global grid
    new_grid = [[-2]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_grid[n-1-j][i] = grid[i][j]
    grid = [row[:] for row in new_grid]

score = 0

while True:
    visited = [[False]*n for _ in range(n)]
    max_block_count = 0
    max_rainbow_count = 0
    max_base_row = -1
    max_base_col = -1
    max_route = []

    # 모든 가능한 그룹 탐색 (시작점은 일반 블록이고 아직 방문하지 않은 것)
    for i in range(n):
        for j in range(n):
            if grid[i][j] > 0 and not visited[i][j]:
                block_count, rainbow_count, base_row, base_col, route = bfs(i, j, visited)
                if block_count == -1:
                    continue
                # 우선순위: block_count(desc) > rainbow_count(desc) > base_row(desc) > base_col(desc)
                if block_count > max_block_count:
                    max_block_count = block_count
                    max_rainbow_count = rainbow_count
                    max_base_row = base_row
                    max_base_col = base_col
                    max_route = route[:]
                elif block_count == max_block_count:
                    if rainbow_count > max_rainbow_count:
                        max_rainbow_count = rainbow_count
                        max_base_row = base_row
                        max_base_col = base_col
                        max_route = route[:]
                    elif rainbow_count == max_rainbow_count:
                        if base_row > max_base_row:
                            max_base_row = base_row
                            max_base_col = base_col
                            max_route = route[:]
                        elif base_row == max_base_row:
                            if base_col > max_base_col:
                                max_base_col = base_col
                                max_route = route[:]

    # 더 이상 제거할 그룹이 없으면 종료
    if max_block_count < 2:
        print(score)
        break

    # 선택된 그룹 제거 & 점수 계산
    for x, y in max_route:
        grid[x][y] = -2
    score += len(max_route) ** 2

    # 중력, 회전, 중력
    gravity()
    rotate_90_counter()
    gravity()