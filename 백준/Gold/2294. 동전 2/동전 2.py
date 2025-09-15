n, k = map(int,input().split())
currencies = list(int(input()) for _ in range(n))
currencies.sort()
INF = int(1e9)
dp = [INF] * (k + 1)
dp[0] = 0

for i in range(1, k + 1):
  for currency in currencies:
    if currency > i:
      continue
    dp[i] = min(dp[i - currency] + 1, dp[i])
    
print(dp[k] if dp[k] != INF else -1)