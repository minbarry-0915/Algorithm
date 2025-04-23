import sys
#sys.stdin = open('input.txt','r')

n,k = map(int, input().split())
dp = [0] * (k + 1)
items = []

for _ in range(n):
    w, v = map(int, input().split())
    items.append((w,v))
for w, v in items:
    for j in range(k, w - 1, -1):
        dp[j] = max(dp[j], dp[j - w] + v)
print(dp[k])