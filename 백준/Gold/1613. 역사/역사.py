import sys
# sys.stdin = open('input.txt','r')

n,k =map(int,input().split())
grid = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(k):
    a,b = map(int, input().split())
    grid[a][b] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j or i == k or k == j:
                continue
            if grid[i][k] == 1 and grid[k][j] == 1:
                grid[i][j] = 1

s = int(input())
for _ in range(s):
    a,b = map(int, input().split())
    if grid[a][b]:
        print(-1)
    elif grid[b][a]:
        print(1)
    else:
        print(0)
