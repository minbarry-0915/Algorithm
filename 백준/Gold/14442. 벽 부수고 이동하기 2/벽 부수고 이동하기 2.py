n,m,k = map(int,input().split())
grid = [list(input().strip()) for _ in range(n)]

from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    queue = deque()
    queue.append((0,0,0,1))
    visited = [[[False] * (k + 1) for _ in range(m)]for _ in range(n)]
    visited[0][0][0] = True
    while queue:
        cx,cy,broken,dist = queue.popleft()

        if cx == n - 1 and cy == m - 1:
            return dist

        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]

            #범위내,미방문,벽 고려
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == '0' and not visited[nx][ny][broken]:
                    visited[nx][ny][broken] = True
                    queue.append((nx,ny,broken, dist + 1))
                elif grid[nx][ny] == '1' and broken < k and not visited[nx][ny][broken + 1]:
                    visited[nx][ny][broken + 1] = True
                    queue.append((nx, ny, broken + 1, dist + 1))
    return -1

print(bfs())