n = int(input())
graph = {i: [] for i in range(1, n + 1)}
dp = [0] * (n + 1)

for i in range(1, n + 1):
    cost, m, *lst = map(int,input().split())
    dp[i] = cost
    for x in lst:
        graph[i].append(x)

for i in range(1, n + 1):
    tmp = 0
    for j in graph[i]:
        tmp = max(tmp, dp[j])
    dp[i] += tmp
print(max(dp))