T = int(input())
dp = [[0] * 31 for _ in range(31)]

for n in range(31):
    for k in range(n + 1):
        if k == 0 or k == n: #0개를 고르거나 전체를 다 고르는 경우는 항상 1가지
            dp[n][k] = 1
        else:
            # n 개중에 1개를 고정하고 이를 A라고 했을때, A가 포함되는 경우와 포함되지 않는 경우를 기반으로 점화식 추출
            # n-1 C r-1 + n-1 C r 이 되는거임
            dp[n][k] = dp[n - 1][k - 1] + dp[n - 1][k]

for _ in range(T):
    n, m = map(int, input().split())
    print(dp[m][n])