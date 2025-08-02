n, k = map(int, input().split())
cost = [list(map(int, input().split())) for _ in range(n)]

# 1. 플로이드 워셜
for m in range(n):
    for i in range(n):
        for j in range(n):
            if cost[i][j] > cost[i][m] + cost[m][j]:
                cost[i][j] = cost[i][m] + cost[m][j]

visited = [False] * n
min_total = int(1e9)

def dfs(now, count, total):
    global min_total
    if count == n:
        min_total = min(min_total, total)
        return

    for next in range(n):
        if not visited[next]:
            visited[next] = True
            dfs(next, count + 1, total + cost[now][next])
            visited[next] = False

visited[k] = True
dfs(k, 1, 0)
print(min_total)