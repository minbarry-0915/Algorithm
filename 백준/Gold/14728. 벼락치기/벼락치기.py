n, t = map(int,input().split())
dp = [0] * (t + 1)
for _ in range(n):
    k,s = map(int,input().split())
    for time in range(t, k - 1, -1):
        dp[time] = max(dp[time], dp[time - k] + s)
print(dp[t])