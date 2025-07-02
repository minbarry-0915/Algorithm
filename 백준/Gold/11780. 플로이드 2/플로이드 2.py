INF = int(1e9)
n = int(input())
m = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

prev = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if c < graph[a][b]:
        graph[a][b] = c
        prev[a][b] = a

for k in range(1, n + 1):
    for  i in range(1, n + 1):
        for j in range(1,n + 1):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                prev[i][j] = prev[k][j]

def get_path(start,end):
    if prev[start][end] == 0:
        return []
    path = []
    curr = end
    while curr != start:
        path.append(curr)
        curr = prev[start][curr]
    path.append(start)
    path.reverse()
    return path

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == 0 or graph[i][j] == INF:
            print(0)
        else:
            path = get_path(i,j)
            print(len(path), * path)
