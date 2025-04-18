import sys
#sys.stdin = open('input.txt','r')
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def dfs(node, total):
    global max_dist, farthest_node
    if total > max_dist:
        max_dist = total
        farthest_node = node

    for neighbor, weight in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            dfs(neighbor, total + weight)

n = int(input().strip())
graph = {i: [] for i in range(n + 1)}

for _ in range(n - 1):
    parent, child, weight = map(int, input().strip().split())
    graph[parent].append((child, weight))
    graph[child].append((parent, weight))

# 1st DFS to find farthest node
visited = [False] * (n + 1)
max_dist = 0
farthest_node = 0
visited[1] = True
dfs(1, 0)

# 2nd DFS to find tree diameter
visited = [False] * (n + 1)
max_dist = 0
visited[farthest_node] = True
dfs(farthest_node, 0)

print(max_dist)
