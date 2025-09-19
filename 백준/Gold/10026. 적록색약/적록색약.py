n = int(input())
grid = [list(input().strip()) for _ in range(n)]

visited1 = [[False] * n for _ in range(n)]
visited2 = [[False] * n for _ in range(n)]

count1 = 0
count2 = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

from collections import deque
def bfs(x,y,initialcolor,visited,isblind):
    queue = deque()
    visited[x][y] = True
    queue.append((x,y))
    while queue:
        cx,cy = queue.popleft()

        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if isblind:
                    if (initialcolor == 'R' and grid[nx][ny] == 'G') or (initialcolor == 'G' and grid[nx][ny] == 'R') or (initialcolor == grid[nx][ny]):
                        visited[nx][ny] = True
                        queue.append((nx,ny))
                else:
                    if initialcolor == grid[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx,ny))
    return 1

for i in range(n):
    for j in range(n):
        if not visited1[i][j]:
            count1 += bfs(i,j,grid[i][j],visited1,False)
        if not visited2[i][j]:
            count2 += bfs(i,j,grid[i][j],visited2,True)

print(count1, count2)
