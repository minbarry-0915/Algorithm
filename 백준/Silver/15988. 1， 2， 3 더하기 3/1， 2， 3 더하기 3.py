import sys
input = sys.stdin.readline

MOD = 1000000009
MAX = 1000000

dp = [0] * (MAX + 1)
dp[1] = 1
dp[2] = 2
dp[3] = 4

# 미리 dp 채우기 (1번만)
for i in range(4, MAX + 1):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MOD

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])
