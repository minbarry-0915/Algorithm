r,c = map(int,input().split())
grid = [list(input().strip()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
count = 0

dx = [-1,0,1]
dy = [1,1,1]

def dfs(x,y):
    if y == c - 1:
        return True

    for d in range(3):
        nx,ny = x + dx[d], y + dy[d]
        if 0 <= nx < r and 0 <= ny < c:
            if grid[nx][ny] == '.' and not visited[nx][ny]:
                visited[nx][ny] = True
                if dfs(nx,ny):
                    return True
    return False

for start_idx in range(r):
    if dfs(start_idx, 0):
        count += 1
print(count)