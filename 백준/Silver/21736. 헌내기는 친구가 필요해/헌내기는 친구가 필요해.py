import sys
# sys.stdin = open('input.txt','r')
input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]
from collections import deque
def bfs(x,y):
    global mx_cnt
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True

    while queue:
        cx,cy = queue.popleft()
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] != 'X':
                if grid[nx][ny] == 'P':
                    mx_cnt += 1
                visited[nx][ny] = True
                queue.append((nx,ny))

n, m = map(int, input().split())
grid = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
mx_cnt = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'I': # 시작지점
            bfs(i,j)
if mx_cnt == 0:
    print('TT')
else:
    print(mx_cnt)