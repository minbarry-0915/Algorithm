from collections import deque
for t in range(1, 11):
    data_len, start = map(int, input().split())
    data = list(map(int, input().split()))

    graph = {i: [] for i in range(1, 101)}
    for i in range(0, data_len, 2):
        u, v = data[i], data[i + 1]
        graph[u].append(v)

    visited = [False] * 101
    queue = deque()
    queue.append((start, 0))

    max_depth = 0
    candidates = []

    while queue:
        now, depth = queue.popleft()

        # 가장 멀리 있는 애 찾아야됨
        if depth > max_depth:
            max_depth = depth
            candidates = [now] # 마지막이 아니기 떄문에 기존 배열 초기화
        elif depth == max_depth:
            candidates.append(now)

        for neighbor in graph[now]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, depth + 1))
    print(f'#{t} {max(candidates)}')