n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]

# 처음 시작
dp[0][0] = grid[0][0]
# 첫번째 행 처리
for j in range(1,m):
    dp[0][j] = dp[0][j - 1] + grid[0][j]
# 첫번째 열 처리
for i in range(1, n):
    dp[i][0] = dp[i - 1][0] + grid[i][0]
# 나머지 처리
for i in range(1,n):
    for j in range(1, m):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + grid[i][j]

print(dp[n - 1][m - 1])