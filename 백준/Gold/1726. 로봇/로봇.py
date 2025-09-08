# 북동남서 시계 방향
dx = [-1,0,1,0]
dy = [0,1,0,-1]

# 방향 재계산 동서남북 -> 북동남서 
def get_real_dir(dir):
  if dir == 1: # 동
    return 1
  elif dir == 2: #서
    return 3
  elif dir == 3: #남
    return 2
  elif dir == 4: #북
    return 0

# 입력
m, n = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(m)]
sx,sy,sd = map(int,input().split())
ex,ey,ed = map(int,input().split())
k = 3 # 이동 가능 거리

# 1-based -> 0-based
sx,sy = sx - 1, sy - 1
ex,ey = ex - 1, ey - 1
# 방향 재할당
sd = get_real_dir(sd)
ed = get_real_dir(ed)

from collections import deque
# 완전 탐색 : bfs
def bfs():
    visited = [[[False]*4 for _ in range(n)] for _ in range(m)]
    queue = deque()
    queue.append((sx, sy, sd, 0))
    visited[sx][sy][sd] = True

    while queue:
        x, y, d, move = queue.popleft()

        if (x, y, d) == (ex, ey, ed):
            return move

        # 좌우 회전
        for nd in [(d-1)%4, (d+1)%4]:
            if not visited[x][y][nd]:
                visited[x][y][nd] = True
                queue.append((x, y, nd, move + 1))

        # 직진 1~3칸
        for dist in range(1, 4):
            nx = x + dx[d]*dist
            ny = y + dy[d]*dist
            if 0 <= nx < m and 0 <= ny < n:
                if grid[nx][ny] == 1:
                    break
                if not visited[nx][ny][d]:
                    visited[nx][ny][d] = True
                    queue.append((nx, ny, d, move + 1))
            else:
                break

print(bfs())