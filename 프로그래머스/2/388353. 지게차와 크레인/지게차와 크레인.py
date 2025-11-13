from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def solution(storage, requests):
    n = len(storage)
    m = len(storage[0])
    new_storage = [['0'] * (m + 2) for _ in range(n + 2)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            new_storage[i][j] = storage[i - 1][j - 1]

    def update():
        nonlocal new_storage
        queue = deque()
        queue.append((0,0))
        visited = [[False] * (m + 2) for _ in range(n + 2)]
        visited[0][0] = True
        
        while queue:
            x,y = queue.popleft()
            
            for d in range(4):
                nx,ny = x + dx[d], y + dy[d]
                if 0 <= nx < n + 2 and 0 <= ny < m + 2 and not visited[nx][ny]:
                    if new_storage[nx][ny] == '0':
                        visited[nx][ny] = True
                        queue.append((nx,ny))
                    elif new_storage[nx][ny] == '1':
                        visited[nx][ny] = True
                        queue.append((nx,ny))
                        new_storage[nx][ny] = '0'
            
    def fork(request):
        buffer = []
        nonlocal new_storage
        for i in range(n + 2):
            for j in range(m + 2):
                if new_storage[i][j] == request:
                    for d in range(4):
                        nx,ny = i + dx[d], j + dy[d]
                        if 0 <= nx < n + 2 and 0 <= ny < m + 2 and new_storage[nx][ny] == '0':
                            buffer.append((i,j))
                            break
        for x,y in buffer:
            new_storage[x][y] = '0'
        update()
        
    def crain(request):
        target = request[0]
        nonlocal new_storage
        buffer = []
        for i in range(n + 2):
            for j in range(m + 2):
                if new_storage[i][j] == target:
                    buffer.append((i,j))
        for x,y in buffer:
            new_storage[x][y] = '1'
        update()
        
        
    for r in requests:
        if len(r) == 1:
            fork(r)
        else:
            crain(r)
            
    for row in new_storage:
        print(row)
        
    cnt = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if new_storage[i][j] != '0' and new_storage[i][j] != '1':
                cnt += 1
    return cnt