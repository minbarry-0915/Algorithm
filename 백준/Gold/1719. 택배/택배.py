import sys
# sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
INF = float('inf')
grid = [[INF] * (n + 1) for _ in range(n + 1)]
floyd = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    grid[i][i] = 0

for _ in range(m):
    a, b, cost = map(int, input().split())
    grid[a][b] = cost
    grid[b][a] = cost
    floyd[a][b] = b
    floyd[b][a] = a

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if grid[i][j] > grid[i][k] + grid[k][j]:
                grid[i][j] = grid[i][k] + grid[k][j]
                floyd[i][j] = floyd[i][k]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(floyd[i][j] if grid[i][j] != 0 else '-', end=' ')
    print()