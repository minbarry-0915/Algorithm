
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def get_nd(d):
    # 상 하 -> 좌우 가능
    # 좌우 -> 상하 가능
    if d in [0, 1]:
        return [2, 3]
    elif d in [2, 3]:
        return [0, 1]


n = int(input())
grid = [list(input()) for _ in range(n)]

door = []

# 문 위치 탐색
for i in range(n):
    for j in range(n):
        if grid[i][j] == '#':
            door.append((i, j))

# 시작,끝 지점
start = door[0]
end = door[1]

# 더 나은 거울 경로 발견시 업데이트하는 visited
visited = [[[int(1e9)] * 4 for _ in range(n)] for _ in range(n)]
heap = []
import heapq

# 초기 위치 각 방향 초기화
for d in range(4):
    nx = start[0] + dx[d]
    ny = start[1] + dy[d]

    # 범위내 미방문 아무것도 없는곳
    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != '*':
        heapq.heappush(heap, (0, nx, ny, d))
        visited[nx][ny][d] = 0

# 경로 탐색
while heap:
    cnt, x, y, d = heapq.heappop(heap)

    if (x, y) == end:  # 문 도착
        continue

    # 현재위치가 거울을 놓을 수 있는 자리인경우, 아닌경우

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

            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != '*':
                if visited[nx][ny][nd] > cnt + 1:  # 최적 경로 발견
                    visited[nx][ny][nd] = cnt + 1
                    heapq.heappush(heap, (cnt + 1, nx, ny, nd))
print(min(visited[end[0]][end[1]]))
