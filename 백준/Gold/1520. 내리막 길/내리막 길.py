import sys
sys.setrecursionlimit(10 ** 5)
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] < grid[x][y]:
            dp[x][y] += dfs(nx,ny)
    return dp[x][y]


n, m = map(int, input().split())  # n,m 바꿈
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]
print(dfs(0,0))