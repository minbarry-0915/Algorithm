n = int(input())
arr = list(map(int, input().split()))

dp = [int(1e9)] * n
dp[0] = 0

for i in range(1, n):
    for j in range(i):
        if j + arr[j] >= i:
            dp[i] = min(dp[i], dp[j] + 1)

print(dp[n - 1] if dp[n - 1] != int(1e9) else -1)
