from collections import deque

# 해당 영역을 가져와서
# 양하고 늑대 갯수 센다음에
# 양이 더 크면 늑대 갯수 감소
# 늑대가 터 크면 양 갯수 감소
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 1

    sheep_cnt = 0
    wolf_cnt = 0
    if grid[i][j] == 'o':
        sheep_cnt += 1
    elif grid[i][j] == 'v':
        wolf_cnt += 1

    while queue:
        cx, cy = queue.popleft()

        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            # 범위내, 미방문, 벽아닐떄
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] != '#':
                if grid[nx][ny] == 'o':
                    sheep_cnt += 1
                elif grid[nx][ny] == 'v':
                    wolf_cnt += 1
                queue.append((nx, ny))
                visited[nx][ny] = 1

    if sheep_cnt > wolf_cnt:
        wolf_cnt = 0
    else:
        sheep_cnt = 0
    return sheep_cnt, wolf_cnt


n, m = map(int, input().split())
total_sheep_cnt = 0
total_wolf_cnt = 0
grid = [list(input().strip()) for _ in range(n)]

visited = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if not visited[i][j] and grid[i][j] != '#':  # 벽이 아니면
            sheep_cnt, wolf_cnt = bfs(i, j)
            total_sheep_cnt += sheep_cnt
            total_wolf_cnt += wolf_cnt
print(total_sheep_cnt, total_wolf_cnt)
