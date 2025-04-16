n = int(input())

dp = [[0] * 10 for _ in range(n + 1)]
dp[1] = [1] * 10
for i in range(2, n + 1):
    for j in range(10):
        if j == 0: # 첫번째 열은 모두 1개
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
print(sum(dp[n]) % 10007)
