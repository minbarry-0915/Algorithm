from collections import deque

def bfs(start):
    queue = deque()
    queue.append((start, 0)) # node, step
    visited = [-1] * (n + 1)
    visited[start] = 0

    while queue:
        current, step = queue.popleft()

        for next in graph[current]:
            if visited[next] == -1:
                visited[next] = step + 1
                queue.append((next, step + 1))

    return visited


n = int(input())
graph = {i: [] for i in range(1, n + 1)}

while True:
    a,b = map(int,input().split())
    if a == -1 and b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)

min_score = int(1e9)
candidates = []
scores = [0]  # 인덱스 맞추기용 (0번은 안 씀)

for i in range(1, n + 1):
    distances = bfs(i)
    score = max(distances[1:])  # 0번 제외
    scores.append(score)

    if score < min_score:
        min_score = score
        candidates = [i]
    elif score == min_score:
        candidates.append(i)

print(min_score, len(candidates))
print(*candidates)