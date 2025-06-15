import sys
# sys.stdin = open('input.txt','r')

v,e = map(int,input().split())
grid = [[int(1e9)] * (v + 1) for _ in range(v + 1)]
for _ in range(e):
    a,b,cost = map(int,input().split())
    grid[a][b] = cost

for k in range(1, v + 1):
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            if grid[i][j] > grid[i][k] + grid[k][j]: # 최적경로 발견
                grid[i][j] = grid[i][k] + grid[k][j]

ans = int(1e9)
for i in range(1, v + 1):
    ans = min(ans, grid[i][i])

print(ans if ans != int(1e9) else -1)