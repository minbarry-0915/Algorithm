
n = int(input())
k = int(input())

# 1번색상을 선택한 경우
dp = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(n + 1):
    for j in range(k + 1):
        if j == 0:
            dp[i][j] = 1
            continue
        if j == 1:
            dp[i][j] = i
            continue
        dp[i][j] += dp[i-1][j]
        dp[i][j] += dp[i-2][j - 1] if i != n else dp[i-3][j-1]

        dp[i][j] %= 1_000_000_003
print(dp[n][k])


