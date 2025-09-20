from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    start = (0,0) #0-based
    end = (n - 1, m - 1)
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    def bfs():
        queue = deque()
        queue.append((start[0], start[1], 1))
        visited = [[False] * m for _ in range(n)]
        visited[0][0] = True
        
        while queue:
            cx,cy,count = queue.popleft()
            if (cx,cy) == end:
                return count
            
            for d in range(4):
                nx, ny = cx + dx[d], cy + dy[d]
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny,count+1))
        return -1
    
    count = bfs()
    return count