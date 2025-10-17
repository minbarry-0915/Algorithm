import sys

sys.setrecursionlimit(10 ** 5)

n,m = map(int,input().split())
managers = list(map(int,input().split()))

graph = {i:[] for i in range(n + 1)}
for i in range(1, n + 1):
    boss = managers[i - 1]
    if boss != -1:
        graph[boss].append(i)

praise = [0] * (n + 1)
for _ in range(m):
    i, w = map(int,input().split())
    praise[i] += w

def dfs(curr):
    for nxt in graph[curr]:
        praise[nxt] += praise[curr]
        dfs(nxt)

dfs(1)
print(*praise[1:])