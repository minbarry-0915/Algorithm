import sys

# sys.stdin = open('input.txt', 'r', encoding='utf-8')


def get_nd(d):
    # 방향: 0-상, 1-하, 2-좌, 3-우
    if d in [0, 1]:  # 상하 → 좌우로 꺾기
        return [2, 3]
    else:            # 좌우 → 상하로 꺾기
        return [0, 1]


n = int(input())
grid = [list(input()) for _ in range(n)]

doors = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == '#':
            doors.append((i, j))

start = doors[0]
end = doors[1]

visited = [[[int(1e9)] * 4 for _ in range(n)] for _ in range(n)]
heap = []
import heapq

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for d in range(4):
    nx = start[0] + dx[d]
    ny = start[1] + dy[d]

    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != '*':
        heapq.heappush(heap, (0, nx, ny, d))
        visited[nx][ny][d] = 0

while heap:
    cnt, x, y, d = heapq.heappop(heap)

    if (x, y) == end:
        continue

    nx = x + dx[d]
    ny = y + dy[d]

    if 0 <= nx < n and 0 <= ny < n:
        if grid[nx][ny] != '*':
            if visited[nx][ny][d] > cnt:  # 최적 경로 발견
                visited[nx][ny][d] = cnt
                heapq.heappush(heap, (cnt, nx, ny, d))

    if grid[x][y] == '!':
        nd_lst = get_nd(d)
        for nd in nd_lst:
            nx = x + dx[nd]
            ny = y + dy[nd]
            # 범위내 벽아님
            if 0 <= nx < n and 0 <= ny < n:
                if grid[nx][ny] != '*':
                    # 더 나은 경로 발견
                    if visited[nx][ny][nd] > cnt + 1:
                        visited[nx][ny][nd] = cnt + 1
                        heapq.heappush(heap, (cnt + 1, nx, ny, nd))
print(min(visited[end[0]][end[1]]))