from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j, target, visited, grid):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 1

    while queue:
        cx, cy = queue.popleft()
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] == target:
                visited[nx][ny] = 1
                queue.append((nx, ny))


n = int(input())
grid_normal = [list(input()) for _ in range(n)]

# 일반 부분 탐색
normal_cnt = 0
visited_normal = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited_normal[i][j]:
            bfs(i, j, grid_normal[i][j], visited_normal, grid_normal)
            normal_cnt += 1

# 적록 색약 버전으로 변경
grid_for_blind = [row[:] for row in grid_normal]
for i in range(n):
    for j in range(n):
        if grid_for_blind[i][j] == 'G':
            grid_for_blind[i][j] = 'R'

# 적록 색약 탐색
visited_blind = [[0] * n for _ in range(n)]
blind_cnt = 0
for i in range(n):
    for j in range(n):
        if not visited_blind[i][j]:
            bfs(i, j, grid_for_blind[i][j], visited_blind, grid_for_blind)
            blind_cnt += 1
print(normal_cnt, blind_cnt)