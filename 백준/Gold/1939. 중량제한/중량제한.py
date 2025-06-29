
n,m = map(int,input().split())
graph = {i: [] for i in range(1,n + 1)}

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

start, end = map(int,input().split())

from collections import deque

def bfs(mid):
    visited = [False] * (n + 1)
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        cur = queue.popleft()
        if cur == end:
            return True

        for nxt, weight in graph[cur]:
            if not visited[nxt] and weight >= mid:
                visited[nxt] = True
                queue.append(nxt)
    return False

left, right = 1, 10 ** 9
result = 0

while left <= right:
    mid = (left + right) // 2

    if bfs(mid):
        result = mid
        left = mid + 1
    else:
        right = mid - 1
print(result)