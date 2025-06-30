n = int(input())
cost = [list(map(int,input().split())) for _ in range(n)]

INF = int(1e9)
answer = INF

for first_color in range(3):
    dp = [[INF] * 3 for _ in range(n)] # 각 집을 해당 컬러로 칠했을때의 최솟값

    dp[0][first_color] = cost[0][first_color]

    for i in range(1, n):
        dp[i][0] = cost[i][0] + min(dp[i - 1][1], dp[i - 1][2])
        dp[i][1] = cost[i][1] + min(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = cost[i][2] + min(dp[i - 1][0], dp[i - 1][1])

    for last_color in range(3):
        if last_color != first_color:
            answer = min(answer, dp[n - 1][last_color])
print(answer)