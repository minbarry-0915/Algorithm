from collections import deque

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited = [[-1] * m for _ in range(n)]
    visited[x][y] = 0
    max_dist = 0

    while q:
        cx, cy = q.popleft()

        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            # 범위내 미방문 육지
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1 and grid[nx][ny] == 'L':
                visited[nx][ny] = visited[cx][cy] + 1
                q.append((nx, ny))
                max_dist = max(max_dist, visited[nx][ny])
    return max_dist


answer = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'L':  # 육지 발견
            # 최장거리 계산
            answer = max(answer, bfs(i, j))
print(answer)