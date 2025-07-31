n = int(input())
start, target = map(int,input().split())
m = int(input())
graph = {i: [] for  i in range(1, n + 1)}
for _ in range(m):
    child,parent = map(int,input().split())
    graph[parent].append(child)
    graph[child].append(parent)

from collections import deque
queue = deque()
visited = [False] * (n + 1)
queue.append((start, 0))
visited[start] = True

result = 0
while queue:
    current, count = queue.popleft()

    if current == target:
        result = count
        break
    for next in graph[current]:
        if not visited[next]:
            queue.append((next, count + 1))
            visited[next] = True

print(result if result else -1)