n, m = map(int,input().split())

weight = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a,b = map(int,input().split())
    weight[a][b] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if weight[i][k] and weight[k][j]:
                weight[i][j] = 1

result = 0
for i in range(1, n + 1):
    heavy = 0
    light = 0
    for j in range(1, n + 1):
        if weight[i][j]:
            light += 1
        if weight[j][i]:
            heavy += 1
    if light > n // 2 or heavy > n // 2:
        result += 1

print(result)