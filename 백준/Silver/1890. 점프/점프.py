n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n -1:
            break
        distance = grid[i][j]
        if 0 <= i + distance < n:
            dp[i + distance][j] += dp[i][j]
        if 0 <= j + distance < n:
            dp[i][j + distance] += dp[i][j]
print(dp[n - 1][n - 1])