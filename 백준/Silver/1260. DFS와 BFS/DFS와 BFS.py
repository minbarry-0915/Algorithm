from collections import deque


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for neighbor in sorted(graph[v]):  # 정점 번호가 작은 것부터 방문
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)


def bfs(graph, start):
    visited = {key: False for key in graph}
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for neighbor in sorted(graph[v]):  # 정점 번호가 작은 것부터 방문
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True


# 입력 받기
n, m, v = map(int, input().split())
graph = {i: [] for i in range(1, n + 1)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS 실행
visited_dfs = {key: False for key in graph}
dfs(graph, v, visited_dfs)
print()

# BFS 실행
bfs(graph, v)
