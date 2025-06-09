import sys
from collections import deque
# sys.stdin = open('input.txt','r')
input = sys.stdin.readline
n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

# 상하좌우 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

group = [[-1] * m for _ in range(n)]  # 각 칸이 속한 그룹 번호
group_size = []  # 각 그룹의 크기

def bfs(x, y, idx):
    queue = deque()
    queue.append((x, y))
    group[x][y] = idx
    size = 1

    while queue:
        cx, cy = queue.popleft()
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == '0' and group[nx][ny] == -1:
                    group[nx][ny] = idx
                    size += 1
                    queue.append((nx, ny))
    return size

# 1. 0인 칸을 그룹화
idx = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == '0' and group[i][j] == -1:
            size = bfs(i, j, idx)
            group_size.append(size)
            idx += 1

# 2. 벽(1) 기준으로 인접한 그룹 크기 합산
result = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if grid[i][j] == '1':
            adj_groups = set()
            total = 1  # 자신을 부순 공간 포함
            for d in range(4):
                ni, nj = i + dx[d], j + dy[d]
                if 0 <= ni < n and 0 <= nj < m:
                    g = group[ni][nj]
                    if g != -1 and g not in adj_groups:
                        total += group_size[g]
                        adj_groups.add(g)
            result[i][j] = total % 10
        else:
            result[i][j] = 0

# 3. 출력
for row in result:
    print(''.join(map(str, row)))
