from collections import deque

def bfs(graph, start):
    queue = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True
    count = 0  # 감염된 컴퓨터 수

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                count += 1  # 감염된 컴퓨터 수 증가
    return count

# 입력 처리
n = int(input())  # 컴퓨터 수 (노드 수)
v = int(input())  # 직접 연결된 컴퓨터 쌍의 수 (간선 수)

graph = {i: [] for i in range(1, n + 1)}

for _ in range(v):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 1번 컴퓨터에서 BFS 실행
print(bfs(graph, 1))
