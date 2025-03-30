import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

directions = [(-1,0), (1,0),(0,-1),(0,1)]

def is_valid(i, j):
    return 0 <= i < n and 0 <= j < m

def dfs(i, j):
    grid[i][j] = 0
    size = 1
    
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if is_valid(ni, nj) and grid[ni][nj] == 1:
            size += dfs(ni, nj)
    
    return size

count = 0
max_size = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            count += 1
            max_size = max(max_size, dfs(i,j))

print(count)
print(max_size)