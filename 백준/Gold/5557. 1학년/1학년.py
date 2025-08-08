
# dp - 메모이제이션

n = int(input())
nums = list(map(int,input().split()))

dp = [[0] * 21 for _ in range(n - 1)] # 마지막 숫자는 결과여야되니까
dp[0][nums[0]] = 1

for i in range(1, n - 1):
    for val in range(21):
        if dp[i - 1][val]:
            plus = val + nums[i]
            minus = val - nums[i]
            if 0 <= plus <= 20:
                dp[i][plus] += dp[i - 1][val]
            if 0 <= minus <= 20:
                dp[i][minus] += dp[i -1][val]

print(dp[n - 2][nums[-1]])