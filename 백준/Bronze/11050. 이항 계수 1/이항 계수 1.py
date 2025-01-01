def binominal_coef(N,K):
    dp = [[0] * (K + 1) for _ in range(N + 1)]

    #C(N,0) = 1 C(N,N) = 1
    for i in range(N + 1):
        dp[i][0] = 1
        if i <= K:
            dp[i][i] = 1

    for n in range(1, N + 1):
        for k in range(1, K + 1):
            #4C3 = 3C2 + 3C3
            dp[n][k] = dp[n-1][k-1] + dp[n-1][k]

    return dp[N][K]

N, K = map(int, input().split())
print(binominal_coef(N, K))