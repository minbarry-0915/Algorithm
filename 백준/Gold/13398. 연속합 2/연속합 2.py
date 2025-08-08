n = int(input())
arr = list(map(int, input().split()))

dp = [[0]*2 for _ in range(n)]
dp[0][0] = arr[0]
dp[0][1] = 0  # 아직 삭제 안 했으니 0

answer = arr[0]

for i in range(1, n):
    dp[i][0] = max(dp[i-1][0] + arr[i], arr[i])
    dp[i][1] = max(dp[i-1][1] + arr[i], dp[i-1][0])
    answer = max(answer, dp[i][0], dp[i][1])

print(answer)