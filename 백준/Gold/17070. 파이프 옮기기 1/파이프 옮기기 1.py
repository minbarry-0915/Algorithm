n= int(input())
grid = [list(map(int,input().split())) for _ in range(n)]

dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]

dp[0][1][0] = 1

for r in range(n):
  for c in range(2, n):
    
    if grid[r][c] == 1:
      continue
    
    # 가로는 이전위치의 가로와 대각선에서 선택가능
    dp[r][c][0] = dp[r][c - 1][0] + dp[r][c - 1][2]
    
    
    # 세로는 이전위치의 세로와 대삭선에서 선택가능
    if r > 0:
      dp[r][c][1] = dp[r - 1][c][1] + dp[r - 1][c][2]
      
    
    # 대각선은 이전위치의 가로세로대각선 모두에서 선택가능
    if r > 0 and grid[r - 1][c] == 0 and grid[r][c - 1] == 0:
      dp[r][c][2] = dp[r - 1][c - 1][0] + dp[r - 1][c - 1][1] + dp[r - 1][c - 1][2]
      
print(sum(dp[n - 1][n - 1]))