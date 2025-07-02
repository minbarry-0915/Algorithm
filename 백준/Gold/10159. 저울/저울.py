n = int(input())
m = int(input())

graph = [[False] * (n +1) for _ in range(n + 1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = True

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = True

for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        if i == j:
            continue
        if not graph[i][j] and not graph[j][i]:
            count += 1
    print(count)