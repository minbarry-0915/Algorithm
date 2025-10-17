t = int(input())
k = int(input())
coins = [tuple(map(int, input().split())) for _ in range(k)]

dp = [0] * (t + 1)
dp[0] = 1

for value, count in coins:
    new_dp = dp[:]  # 기존 dp 보존
    for money in range(t + 1):
        if dp[money] == 0:
            continue
        for c in range(1, count + 1):
            next_money = money + value * c
            if next_money > t:
                break
            new_dp[next_money] += dp[money]
    dp = new_dp

print(dp[t])