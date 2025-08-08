s1 = list(input().strip())
n1 = len(s1)
s2 = list(input().strip())
n2 = len(s2)

dp = [[0] * (n1 + 1) for _ in range(n2 + 1)]
answer = 0

for i in range(1, n2 + 1):
    for j in range(1, n1 + 1):
        if s2[i - 1] == s1[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            if dp[i][j] > answer:
                answer = dp[i][j]
        else:
            dp[i][j] = 0
            
print(answer)