import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = {i: [] for i in range(1, n + 1)}
visited = {i: False for i in range(1, n + 1)}

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs(start):
    queue = deque([start])
    count = 0
    while queue:
        current = queue.popleft()
        visited[current] = True
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1

    return count

print(bfs(1))