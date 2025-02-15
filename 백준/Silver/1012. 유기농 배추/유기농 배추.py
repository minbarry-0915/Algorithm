# 1012 유기농 배추
import sys
sys.setrecursionlimit(10000)
def dfs(graph, x,y,m,n):
    if x < 0 or x >= m or y < 0 or y >= n or graph[x][y] == 0:
        return
    graph[x][y] = 0

    dfs(graph,x-1,y,m,n)
    dfs(graph,x+1,y,m,n)
    dfs(graph,x,y-1,m,n)
    dfs(graph,x,y+1,m,n)
    

t = int(input())

for test in range(t):
    m, n, k = map(int, input().split())

    graph = [[0 for _ in range(n + 1)] for _ in range(m + 1) ]

    for _ in range(k):
        x,y = map(int, input().split())
        graph[x][y] = 1

    count = 0 #흰지렁이
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                count += 1
                dfs(graph, i, j, m, n)
    print(count)