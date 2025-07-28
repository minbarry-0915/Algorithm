import sys
from collections import deque

# sys.stdin = open('input.txt', 'r', encoding='utf-8')
input = sys.stdin.readline

m,n = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

sx, sy = 0, 0
item_index = {}
idx = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == 'S':
            sx, sy = i, j
        elif grid[i][j] == 'X':
            item_index[(i, j)] = idx
            idx += 1

total_items = idx
visited = [[[False] * (1 << total_items) for _ in range(m)] for _ in range(n)]
queue = deque()
queue.append((sx, sy, 0, 0))  # x, y, collected_items, time
visited[sx][sy][0] = True

while queue:
    x, y, check, time = queue.popleft()

    if grid[x][y] == 'E' and check == (1 << total_items) - 1:
        print(time)
        break

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]

        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != '#':
            new_check = check
            if grid[nx][ny] == 'X':
                item_num = item_index[(nx, ny)]
                new_check |= (1 << item_num)

            if not visited[nx][ny][new_check]:
                visited[nx][ny][new_check] = True
                queue.append((nx, ny, new_check, time + 1))
