from collections import deque
def bfs(start):
    visited = [0] * (n + 1)
    visited[start] = 1
    count = 1
    queue = deque()
    queue.append(start)

    while queue:
        current = queue.popleft()

        for next in graph[current]:
            if not visited[next]:
                visited[next] = count + 1
                count += 1
                queue.append(next)

    return visited

n,m, start = map(int,input().split())
graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    graph[i].sort(reverse=True)

result = bfs(start)
for i in range(1, n + 1):
    print(result[i])