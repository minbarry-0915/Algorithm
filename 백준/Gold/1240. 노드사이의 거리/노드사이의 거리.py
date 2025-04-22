import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def dfs(current, target, distance):
    if current == target:
        return distance

    for neighbor, cost in graph[current]:
        if not visited[neighbor]:
            visited[neighbor] = True
            result = dfs(neighbor, target, distance + cost)
            if result is not None:
                return result
    return None

n, m = map(int, input().split())
graph = {i: [] for i in range(n + 1)}

for _ in range(n - 1):
    a,b,cost = map(int,input().split())
    graph[a].append((b,cost))
    graph[b].append((a,cost))

for _ in range(m):
    a,b = map(int,input().split())
    visited = [False] * (n + 1)
    visited[a] = True
    print(dfs(a,b,0))