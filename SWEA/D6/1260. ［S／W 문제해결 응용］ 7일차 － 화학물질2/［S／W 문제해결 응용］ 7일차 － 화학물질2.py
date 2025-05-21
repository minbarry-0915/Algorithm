
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, visited, matrix):
    queue = deque()
    visited[x][y] = True
    queue.append((x, y))
    xs = set()
    ys = set()

    while queue:
        cx, cy = queue.popleft()
        xs.add(cx)
        ys.add(cy)
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and matrix[nx][ny] != 0:
                visited[nx][ny] = True
                queue.append((nx, ny))

    row = max(xs) - min(xs) + 1
    col = max(ys) - min(ys) + 1
    return row, col


def matrix_chain_order(matricies):
    n = len(matricies)

    indegree = [0] * n
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and matricies[i][1] == matricies[j][0]:
                graph[i].append(j)
                indegree[j] += 1

    # 시작점 찾기
    start = -1
    for i in range(n):
        if indegree[i] == 0:
            start = i
            break

    # 순서 찾기, 위상 정렬
    order = []
    visited = [False] * n

    def dfs(u):
        order.append(u)
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs(v)

    dfs(start)

    # DP 설정
    size = len(order)
    dp = [[0] * size for _ in range(size)]
    dims = []
    dims.append(matricies[order[0]][0])
    for idx in order:
        dims.append(matricies[idx][1])

    for l in range(2, size + 1):
        for i in range(size - l + 1):
            j = i + l - 1
            dp[i][j] = int(1e9)
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
    return dp[0][size - 1]


T = int(input())
for t in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    submatrix_lst = []
    # 덩어리 추출
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and matrix[i][j] != 0:
                row, col = bfs(i, j, visited, matrix)
                submatrix_lst.append((row, col))
    # 행렬 곱 최소 연산 계산
    result = matrix_chain_order(submatrix_lst)

    print(f'#{t} {result}')