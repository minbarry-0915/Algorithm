def solution(info, n, m):
    INF = float('inf')
    size = len(info)
    
    dp = [[INF] * m for _ in range(size + 1)]
    dp[0][0] = 0
    
    for i in range(1, size + 1):
        a_score = info[i - 1][0]
        b_score = info[i - 1][1]
        
        for j in range(m):
            # a가 훔칠시
            a_total = dp[i - 1][j] + a_score
            if a_total < n:
                dp[i][j] = min(dp[i][j], a_total)
            # b가 훔칠시
            b_total = j + b_score
            if b_total < m:
                dp[i][b_total] = min(dp[i][b_total], dp[i - 1][j])
    print(dp[size])
    
    answer = INF
    for value in dp[size]:
        answer = min(answer, value)
        
    return answer if answer != INF else -1