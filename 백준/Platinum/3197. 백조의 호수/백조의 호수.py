from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

r,c = map(int,input().split())
grid = [list(input().strip()) for _ in range(r)]

water_queue = deque()
swans = []

for i in range(r):
  for j in range(c):
    if grid[i][j] == 'L':
      swans.append((i,j))

    if grid[i][j] != 'X':
      water_queue.append((i,j))

swan_queue = deque()
next_swan_queue = deque()
swan_visited = [[False] * c for _ in range(r)]

sx,sy = swans[0]
swan_queue.append((sx,sy))
swan_visited[sx][sy] = True

def can_move():
  while swan_queue:
    x,y = swan_queue.popleft()
    if (x,y) == swans[1]:
      return True

    for d in range(4):
      nx,ny = x + dx[d], y + dy[d]
      if 0 <= nx < r and 0 <= ny < c and not swan_visited[nx][ny]:
        swan_visited[nx][ny] = True
        if grid[nx][ny] != 'X':
          swan_queue.append((nx,ny))
        elif grid[nx][ny] == 'X':
          next_swan_queue.append((nx,ny))
  return False

def melt_ice():
  size = len(water_queue)
  for _ in range(size):
    x,y = water_queue.popleft()
    for d in range(4):
      nx,ny = x + dx[d], y + dy[d]
      if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == 'X':
        grid[nx][ny] = '.'
        water_queue.append((nx,ny))
time = 0
while True:
  if can_move():
    print(time)
    break
  melt_ice()

  swan_queue = next_swan_queue
  next_swan_queue = deque()
  time += 1
