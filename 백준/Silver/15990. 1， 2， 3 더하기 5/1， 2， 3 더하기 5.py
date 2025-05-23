MOD = 1000000009
MAX = 100001

# dp[n][k]: n을 만드는 방법 중, 마지막 숫자가 k인 경우
dp = [[0] * 4 for _ in range(MAX)]

# 초기값
dp[1][1] = 1
dp[2][2] = 1
dp[3][1] = 1
dp[3][2] = 1
dp[3][3] = 1

# 점화식 채우기
for i in range(4, MAX):
    dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % MOD
    dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % MOD
    dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % MOD

T = int(input())
for _ in range(T):
    n = int(input())
    print((dp[n][1] + dp[n][2] + dp[n][3]) % MOD)