import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}

for i in range (1, m + 1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for key in graph:
    graph[key].sort()

visited_dfs = {i: False for i in range(1, n + 1)}

def dfs(v):
    visited_dfs[v] = True
    print(v, end=' ')
    for neighbor in graph[v]:
        if not visited_dfs[neighbor]:
            dfs(neighbor)

visited_bfs = {i: False for i in range(1, n + 1)}

def bfs(start):
    queue = deque([start])
    visited_bfs[v] = True
    while queue:
        current = queue.popleft()
        print(current, end= ' ')
        for neighbor in graph[current]:
            if not visited_bfs[neighbor]:
                visited_bfs[neighbor] = True
                queue.append(neighbor)
                
dfs(v)
print()
bfs(v)

