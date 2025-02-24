from collections import deque

n = int(input())  # 전체 사람 수
x, y = map(int, input().split())  # 촌수를 계산할 두 사람
m = int(input())  # 관계의 개수

# 그래프를 인접 리스트로 표현
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    parent, child = map(int, input().split())
    graph[parent].append(child)
    graph[child].append(parent)  # 양방향 연결

# BFS 탐색
def bfs(start, target):
    queue = deque([(start, 0)])  # (현재 노드, 촌수)
    visited = [False] * (n + 1)
    visited[start] = True

    while queue:
        current, count = queue.popleft()

        if current == target:  # 목표 노드에 도착하면 촌수 반환
            return count

        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, count + 1))

    return -1  # 목표 노드에 도달할 수 없는 경우

# 결과 출력
print(bfs(x, y))
