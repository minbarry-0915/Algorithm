import sys

# sys.stdin = open('input.txt', 'r', encoding='utf-8')

input = sys.stdin.readline

n, m = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

total_cost = sum(cost)
dp = [[0] * (total_cost + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    mem = memory[i - 1]
    c = cost[i - 1]

    for j in range(total_cost + 1):
        if j < c:  # 현재 앱을 종료하지 않을 때은 기존 메모리
            dp[i][j] = dp[i - 1][j]
        else:  # 현재 앱을 종료하면 얻을수있는 최대 메모리
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - c] + mem)

for j in range(total_cost + 1):
    if dp[n][j] >= m:
        print(j)
        break