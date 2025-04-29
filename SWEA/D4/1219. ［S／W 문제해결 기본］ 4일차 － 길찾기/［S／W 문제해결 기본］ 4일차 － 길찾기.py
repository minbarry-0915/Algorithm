from collections import deque
def bfs(start,target, graph):
    visited = {i: False for i in range(100)}
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        current = queue.popleft()
        if current == target:
            return 1
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return 0



start, target = 0, 99
for _ in range(10):
    t_num, n = map(int, input().split())
    pair_lst = list(map(int, input().split()))
    graph = {i: [] for i in range(100)}
    for i in range(0, 2 * n, 2):
        x, y = pair_lst[i], pair_lst[i + 1]
        graph[x].append(y)
    result = bfs(start, target, graph)
    print(f'#{t_num} {result}')