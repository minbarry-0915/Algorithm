n = int(input())
t = [0] * (n + 1)
p = [0] * (n + 1)
dp = [0] * (n + 2)

for i in range(1, n + 1):
    t[i], p[i] = map(int, input().split())

for i in range(1, n + 1):
    dp[i] = max(dp[i], dp[i - 1])

    if i + t[i] - 1 <= n:
        dp[i + t[i]] = max(dp[i + t[i]], dp[i] + p[i])

print(max(dp))