import sys
from collections import deque

# sys.stdin = open('input.txt', 'r', encoding='utf-8')
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

# 시작 위치 찾기
for i in range(n):
    for j in range(m):
        if grid[i][j] == '0':
            sx, sy = i, j

# 방문 배열: (x, y, 열쇠 상태)
visited = [[[False] * (1 << 6) for _ in range(m)] for _ in range(n)]
queue = deque()
queue.append((sx, sy, 0, 0))  # x, y, keys, cnt
visited[sx][sy][0] = True

while queue:
    x, y, keys, cnt = queue.popleft()

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if not (0 <= nx < n and 0 <= ny < m):
            continue
        cell = grid[nx][ny]
        if cell == '#':
            continue

        new_keys = keys

        # 열쇠
        if 'a' <= cell <= 'f':
            new_keys |= (1 << (ord(cell) - ord('a')))

        # 문
        if 'A' <= cell <= 'F':
            if not (keys & (1 << (ord(cell) - ord('A')))):
                continue

        # 방문 체크
        if visited[nx][ny][new_keys]:
            continue
        visited[nx][ny][new_keys] = True

        # 도착지 도달
        if cell == '1':
            print(cnt + 1)
            exit()

        queue.append((nx, ny, new_keys, cnt + 1))

# 도달 불가능
print(-1)
