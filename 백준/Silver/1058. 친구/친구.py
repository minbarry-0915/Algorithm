import sys
# sys.stdin = open('input.txt','r')

n = int(input())
grid = [list(input().strip()) for _ in range(n)]

matrix = [[0] * n for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if grid[i][j] == 'Y' or (grid[i][k] == 'Y' and grid[k][j] == 'Y'):
                matrix[i][j] = 1

res = 0

for row in matrix:
    res = max(res, sum(row))
print(res)