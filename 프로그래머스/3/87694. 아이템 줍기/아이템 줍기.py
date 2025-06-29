from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    MAX = 102
    grid = [[-1] * MAX for _ in range(MAX)]
    visited = [[0] * MAX for _ in range(MAX)]
    
    for elem in rectangle: 
        lx,ly,rx,ry = map(lambda x:x*2, elem)
        for i in range(lx, rx + 1):
            for j in range(ly, ry + 1):
                if lx < i < rx and ly < j < ry:
                    grid[i][j] = 0
                elif grid[i][j] != 0: # 이미 내부임 -> 테두리 처리 할 필요없음
                    grid[i][j] = 1
                    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    q = deque()
    q.append((characterX * 2, characterY * 2))
    while q:
        x,y = q.popleft()
        if x == itemX * 2 and y == itemY * 2: # 도착
            answer = visited[x][y] // 2
            return answer
        
        for d in range(4):
            nx,ny = x + dx[d], y + dy[d]
            if 0 < nx < MAX and 0 < ny < MAX and not visited[nx][ny]:
                if grid[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
                    
    return answer
    