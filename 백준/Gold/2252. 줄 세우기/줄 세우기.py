n,m = map(int,input().split())

graph = {i: [] for i in range(1, n + 1)}
indegree = [0] * (n + 1)

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1


from collections import deque
q = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)


result = []

while q:
    current = q.popleft()
    result.append(current)

    for next in graph[current]:
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)
print(*result)