import sys
input = sys.stdin.readline

n = int(input())  # n을 입력받음

MOD = 10007  # 결과를 10007로 나눈 나머지를 구함
dp = [0] * (n + 1)

# 초기값 설정
dp[1] = 1
if n > 1:
    dp[2] = 2

# dp[n]을 구하는 반복문
for i in range(3, n + 1):
    dp[i] = (dp[i-1] + dp[i-2]) % MOD

print(dp[n])  # n번째 값 출력
