import sys
sys.setrecursionlimit(10 ** 6)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    if dp[x][y]:
        return dp[x][y]

    dp[x][y] = 1
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < n and 0 <= ny < n and grid[x][y] < grid[nx][ny]:
            dp[x][y] = max(dp[x][y], dfs(nx,ny) + 1)
    return dp[x][y]


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

result = 0
for i in range(n):
    for j in range(n):
        result = max(result, dfs(i, j))

print(result)
