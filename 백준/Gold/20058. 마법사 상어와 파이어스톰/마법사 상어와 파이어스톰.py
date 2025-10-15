n,q = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(2**n)]
# print(grid)
l_arr = list(map(int,input().split()))

def rotate_90(sx,sy,l):
    part = [row[sy:sy + l] for row in grid[sx:sx + l]]

    # 90도 회전
    new_part = [[0] * l for _ in range(l)]
    for i in range(l):
        for j in range(l):
            new_part[j][l - 1 - i] = part[i][j]

    # 그리드 업데이트
    for i in range(l):
        for j in range(l):
            grid[sx + i][sy + j] = new_part[i][j]
    return

dx = [-1,1,0,0]
dy = [0,0,-1,1]

from collections import deque
def bfs(x,y,visited):
    queue = deque()
    queue.append((x,y))
    cnt = 1
    visited[x][y] = True

    while queue:
        cx,cy = queue.popleft()

        for d in range(4):
            nx,ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < 2 ** n and 0 <= ny < 2 ** n and not visited[nx][ny] and grid[nx][ny] != 0:
                visited[nx][ny] = True
                queue.append((nx,ny))
                cnt += 1
    return cnt

# q 만큼 반복
for qi in range(q):
    l = 2 ** l_arr[qi]

    # 부분 격자 쪼개기 (매 단계마다 범위가 다름)
    # 부분 격자 90도 회전 반영
    for i in range(0, 2**n, l):
        for j in range(0, 2**n, l):
            rotate_90(i,j,l)
    # 인접 조건 만족하지 않는 얼음의 양 감소
    # 얼음이 있는 칸 3개 이상과 인접하지 않은 칸은 얼음의 양이 1 줄어들음
    # 감소 시킬 얼음 위치 수집
    to_decrease = []
    for i in range(2 ** n):
        for j in range(2 ** n):
            if grid[i][j] == 0:
                continue

            adj_ice_cnt = 0
            for d in range(4):
                nx,ny = i + dx[d], j + dy[d]
                if 0 <= nx < 2 ** n and 0 <= ny < 2 ** n:
                    if grid[nx][ny] != 0:
                        adj_ice_cnt += 1

            if adj_ice_cnt < 3:
                to_decrease.append((i,j))
    # 감소 처리
    for i,j in to_decrease:
        if grid[i][j] > 0:
            grid[i][j] -= 1

# 반복후에 남아있는 얼음의 합계산
total_ice = sum(sum(row) for row in grid)
print(total_ice)

# 덩어리 크기 추적 bfs()
visited = [[False] * (2 ** n) for _ in range(2 ** n)]
max_ice_cnt = 0
for i in range(2 ** n):
    for j in range(2 ** n):
        if not visited[i][j] and grid[i][j] != 0:
            ice_cnt = bfs(i,j,visited)
            max_ice_cnt = max(max_ice_cnt, ice_cnt)
print(max_ice_cnt)