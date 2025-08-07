n, m = map(int,input().strip().split())

grid = []
grid.append(['0'] * (m + 1))
for _ in range(n):
  grid.append(list('0' + input().strip()))

dp = [[0] * (m + 1) for _ in range(n + 1)]

max_len = 0
for i in range(1,n + 1):
  for j in range(1,m + 1):
    if grid[i][j] == '1':
      dp[i][j] = min(
        dp[i-1][j],     # 위
        dp[i][j-1],     # 왼쪽
        dp[i-1][j-1]    # 왼쪽 위
        ) + 1
      max_len = max(max_len, dp[i][j])

print(max_len ** 2)