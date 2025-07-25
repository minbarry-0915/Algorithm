n = int(input())

dp = [0]*(n+1)
if n  >= 2:
    dp[2] = 3

for i in range(4,n+1,2):
    dp[i] = dp[i-2] *dp[2] + sum(dp[2: i - 4 + 1] * 2) + 2
print(dp[n])