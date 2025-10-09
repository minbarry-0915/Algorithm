INF = int(1e9)
def solution(alp, cop, problems):
    max_alp_req = max([p[0] for p in problems])
    max_cop_req = max([p[1] for p in problems])
    
    dp = [[INF] * (max_cop_req + 1) for _ in range(max_alp_req + 1)]
    alp = min(alp, max_alp_req)
    cop = min(cop, max_cop_req)
    dp[alp][cop] = 0

    for i in range(alp, max_alp_req + 1):
        for j in range(cop, max_cop_req + 1):
            # 알고리즘 공부
            next_i = min(i + 1, max_alp_req)
            dp[next_i][j] = min(dp[next_i][j], dp[i][j] + 1)
            # 코딩 공부
            next_j = min(j + 1, max_cop_req)
            dp[i][next_j] = min(dp[i][next_j], dp[i][j] + 1)
            # 문제 풀이
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i < alp_req or j < cop_req:
                    continue
                next_alp = min(i + alp_rwd, max_alp_req)
                next_cop = min(j + cop_rwd, max_cop_req)
                dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j] + cost)
    
    answer = dp[max_alp_req][max_cop_req]
    return answer