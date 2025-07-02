n,m,r = map(int,input().split())
items = [0] + list(map(int, input().split()))
costs = [[int(1e9)] * (n + 1) for _ in range(n+1)]

for i in range(1, n + 1):
    costs[i][i] = 0 # 자기 자신

for _ in range(r):
    a,b,c = map(int,input().split())
    costs[a][b] = min(costs[a][b], c)
    costs[b][a] = min(costs[b][a], c)

for k in range(1, n + 1):        # 거쳐가는 노드
    for i in range(1, n + 1):    # 출발 노드
        for j in range(1, n + 1):# 도착 노드
            if costs[i][j] > costs[i][k] + costs[k][j]:
                costs[i][j] = costs[i][k] + costs[k][j]

max_items = 0
for i in range(1, n + 1):
    total = 0
    for j in range(1, n + 1):
        if costs[i][j] <= m:
            total += items[j]
    max_items = max(max_items, total)
print(max_items)