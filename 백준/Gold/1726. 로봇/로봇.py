from collections import deque
# 동 남 서 북
dx = [0,1,0,-1]
dy = [1,0,-1,0]

direction_to_index = {
  1: 0,
  2: 2,
  3: 1,
  4: 3
}

n,m = map(int,input().split())

grid = [list(map(int,input().split())) for _ in range(n)]
sx,sy,sd = map(int,input().split())
sx,sy,sd = sx - 1,sy - 1,direction_to_index[sd] # 0 - index, 동남서북 기준으로 변환
ex,ey,ed = map(int,input().split())
ex,ey,ed = ex - 1,ey - 1,direction_to_index[ed]  # 0 - index

visited = [[[-1] * 4 for _ in range(m)] for _ in range(n)]

queue = deque()
queue.append((sx,sy,sd,0))
visited[sx][sy][sd] = 0

while queue:
  x,y,cd,cnt = queue.popleft()

  if x == ex and y == ey and cd == ed:
    print(visited[ex][ey][ed])
    break
  
  # 1,2,3 만큼 직진 
  for k in range(1,4):
    nx = x + k * dx[cd]
    ny = y + k * dy[cd]
    
    if not (0 <= nx < n and 0 <= ny < m):
        break
    if grid[nx][ny] == 1:
        break
    if visited[nx][ny][cd] == -1:
        visited[nx][ny][cd] = cnt + 1
        queue.append((nx,ny,cd,cnt + 1))

  # 오른쪽 회전
  nd = (cd + 1) % 4
  if visited[x][y][nd] == -1:
    visited[x][y][nd] = cnt + 1
    queue.append((x,y,nd,cnt + 1))
  
  # 왼쪽 회전
  nd = (cd - 1) % 4
  if visited[x][y][nd] == -1:
    visited[x][y][nd] = cnt + 1
    queue.append((x,y,nd,cnt + 1))

