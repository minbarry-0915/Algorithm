n = int(input())
t = [0]
p = [0]
for _ in range(n):
    a,b = map(int,input().split())
    t.append(a)
    p.append(b)
    
dp = [0] * (n + 2)

for i in range(1, n + 1):
    # 상담을 할수 있는경우
    if i + t[i] - 1 <= n:
        dp[i + t[i] - 1] = max(dp[i + t[i] - 1], dp[i - 1] + p[i])
    # 상담을 하지 않고 다음 날로 넘기는 경우
    dp[i] = max(dp[i], dp[i - 1])
print(dp[n])