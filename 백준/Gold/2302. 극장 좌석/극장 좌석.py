n = int(input())
m = int(input())
dp = [0] * (n + 1)
dp[0] = 1
dp[1] = 1
for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

answer = 1
pre = 0
for i in range(m):
    k = int(input())
    answer *= dp[k - pre - 1]
    pre = k
answer *= dp[n - pre]
print(answer)