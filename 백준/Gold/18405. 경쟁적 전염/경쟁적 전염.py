from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
S, X, Y = map(int, input().split())

# 1. 초기 바이러스 수집 (시간 0초)
virus = []
for i in range(n):
    for j in range(n):
        if grid[i][j] != 0:
            virus.append((0, grid[i][j], i, j))  # (시간, 바이러스 번호, x, y)

# 2. 바이러스 번호 낮은 순서 정렬
virus.sort(key=lambda v: v[1])

# 3. BFS 시작
queue = deque(virus)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    time, vnum, x, y = queue.popleft()

    # S초가 지나면 중단
    if time == S:
        break

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
            grid[nx][ny] = vnum
            queue.append((time + 1, vnum, nx, ny))

# 4. 결과 출력 (문제는 1-indexed)
print(grid[X - 1][Y - 1])