import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
from collections import deque

def bfs(i):
    visited = [False] * (n + 1)
    queue = deque()
    queue.append(i)

    visited[i] = True
    cnt = 1

    while queue:
        c = queue.popleft()
        for neighbor in graph[c]:
            if not visited[neighbor]:
                cnt +=1
                visited[neighbor] = True
                queue.append(neighbor)

    # 역방향 탐색
    visited = [False] * (n + 1)
    visited[i] = True
    queue.append(i)
    while queue:
        c = queue.popleft()
        for neighbor in graph_reversed[c]:
            if not visited[neighbor]:
                cnt += 1
                visited[neighbor] = True
                queue.append(neighbor)

    return cnt

n, m = map(int, input().split())
graph = {i: [] for i in range(n + 1)}  # 작은 쪽 탐색용
graph_reversed = {i: [] for i in range(n + 1)}  # 큰쪽 탐색용

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph_reversed[b].append(a)
total = 0
for i in range(1, n + 1):
    cnt = bfs(i)
    if cnt == n:
        total += 1
print(total)
