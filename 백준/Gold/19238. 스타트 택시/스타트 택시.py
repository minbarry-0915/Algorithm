import sys
from collections import deque

# 입력
N, M, fuel = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 택시 위치 (0-index)
tx, ty = map(int, input().split())
tx -= 1
ty -= 1

# 승객 정보: 출발지 -> (도착지)
passengers = dict()
for _ in range(M):
    sx, sy, ex, ey = map(int, input().split())
    passengers[(sx - 1, sy - 1)] = (ex - 1, ey - 1)

# 상하좌우
DIRS = [(-1, 0), (0, -1), (0, 1), (1, 0)]  # 행 우선 타이브레이크를 위해 상,좌,우,하로 두지 않아도 정렬로 보장
# 하지만 일반적으로 상좌우하로 두고, 나중에 후보를 정렬(행,열)하면 된다.

def bfs_distance(start_x, start_y):
    """(start_x, start_y)에서 모든 칸까지의 최단거리(-1: 불가)를 반환"""
    dist = [[-1] * N for _ in range(N)]
    q = deque()
    q.append((start_x, start_y))
    dist[start_x][start_y] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in [(-1,0),(0,-1),(0,1),(1,0)]:  # 상좌우하 (거리 동일 시 행,열 작은 승객을 고르기 유리)
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
    return dist

def pick_passenger(tx, ty):
    """
    현재 택시 위치에서 태울 승객을 고른다.
    반환: (승객출발x, 승객출발y, dist_to_passenger) 또는 (None, None, -1) (태울 승객 없음)
    """
    dist = bfs_distance(tx, ty)

    # 태울 수 있는 승객 후보 수집
    candidates = []
    for (sx, sy), _ in passengers.items():
        d = dist[sx][sy]
        if d != -1:  # 도달 가능
            candidates.append((d, sx, sy))

    if not candidates:
        return None, None, -1

    # 거리, 행, 열 오름차순
    candidates.sort()
    d, sx, sy = candidates[0]
    return sx, sy, d

def drive(sx, sy, ex, ey):
    """
    (sx, sy)에서 (ex, ey)까지 최단거리. 불가 시 -1
    """
    dist = bfs_distance(sx, sy)
    return dist[ex][ey]

# 시뮬레이션
for _ in range(M):
    # 1) 가장 가까운 승객 찾기
    psx, psy, d_to_p = pick_passenger(tx, ty)
    if d_to_p == -1 or fuel - d_to_p < 0:
        print(-1)
        sys.exit(0)

    # 택시가 승객 위치로 이동
    fuel -= d_to_p
    tx, ty = psx, psy

    # 2) 승객 목적지까지 이동
    destx, desty = passengers[(psx, psy)]
    d_to_dest = drive(psx, psy, destx, desty)
    if d_to_dest == -1 or fuel - d_to_dest < 0:
        print(-1)
        sys.exit(0)

    # 성공적으로 도착: 연료 보충 (소모한 d_to_dest의 2배 충전 → 순증가 d_to_dest)
    fuel -= d_to_dest
    fuel += 2 * d_to_dest

    # 승객 하차 및 제거
    tx, ty = destx, desty
    del passengers[(psx, psy)]

# 모든 승객 이동 완료
print(fuel)
