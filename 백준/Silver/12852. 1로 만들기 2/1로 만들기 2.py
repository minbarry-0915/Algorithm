import sys

# sys.stdin = open('input.txt', 'r')

n = int(input())
dp = [0] * (n + 1)
path = [0] * (n + 1)

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + 1
    path[i] = i - 1
    # 최적 경로 비교
    if i % 2 == 0 and dp[i // 2] + 1 < dp[i]:
        dp[i] = dp[i // 2] + 1
        path[i] = i // 2
    if i % 3 == 0 and dp[i // 3] + 1 < dp[i]:
        dp[i] = dp[i // 3] + 1
        path[i] = i // 3

print(dp[n])
result = []
current = n
while current != 0:
    result.append(current)
    current = path[current]

print(*result)
