import sys
from collections import deque

# 입력
n, m, fuel = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 택시 위치
tx,ty = map(int,input().split())
tx -= 1
ty -= 1

# 승객 위치
customers = dict()
for _ in range(m):
    sx,sy,ex,ey = map(int,input().split())
    customers[(sx - 1,sy - 1)] = (ex - 1, ey - 1)

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def get_distance(tx,ty):
    queue = deque()
    visited = [[-1] * n for _ in range(n)]
    queue.append((tx,ty))
    visited[tx][ty] = 0

    while queue:
        x,y = queue.popleft()

        for d in range(4):
            nx,ny = x + dx[d], y + dy[d]
            # 범위내 미방문 벽아닌곳
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1 and grid[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))

    return visited

def pick_customer(tx,ty):
    dist_grid = get_distance(tx,ty) # 모든 지점에 대한 최적 경로

    candidates = []
    for (sx,sy), _ in customers.items():
        dist = dist_grid[sx][sy]
        if dist != -1: #도달 가능
            candidates.append((dist,sx,sy)) # 추후 정렬 비교시 원활

    if not candidates:
        return None, None, -1

    candidates.sort(key= lambda x: (x[0],x[1],x[2]))
    dist_to_c,cx,cy = candidates[0]# 거리, 행, 열 순으로 정렬
    return cx,cy,dist_to_c

def drive(sx,sy,ex,ey):
    dist_grid = get_distance(sx,sy)
    return dist_grid[ex][ey]

# 택시 위치 기준 최적경로를 찾고
# 가장 짧은 경로의 손님을 골라서
# 목적지로 이동, fuel 감소
# -1은 fuel 이 음수거나, 손님이 남았는데 태울수없을때
# 모든 손님을 다 태우면 남은 연로 출력

for _ in range(m):
    cx,cy,dist_to_c = pick_customer(tx,ty)
    if dist_to_c == -1 or fuel - dist_to_c < 0:
        print(-1)
        sys.exit(0)

    fuel -= dist_to_c
    tx,ty = cx,cy # 손님을 태움

    # 목적지로 이동
    destx,desty = customers[(cx,cy)]
    dist_to_dest = drive(tx,ty,destx,desty)

    if dist_to_dest == -1 or fuel - dist_to_dest < 0:
        print(-1)
        sys.exit(0)

    # 도착 완료
    fuel -= dist_to_dest
    fuel += dist_to_dest * 2

    tx,ty = destx,desty
    del customers[(cx,cy)]
print(fuel)