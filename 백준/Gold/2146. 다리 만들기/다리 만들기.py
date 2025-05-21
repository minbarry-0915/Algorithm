from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 1. 섬에 고유 번호 붙이기
def label_islands():
    island_id = 2  # 1은 기존 육지, 2부터 고유 섬 번호 부여
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                bfs_label(i, j, island_id)
                island_id += 1


def bfs_label(x, y, island_id):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = island_id

    while queue:
        cx, cy = queue.popleft()
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = island_id
                queue.append((nx, ny))


# 2. 각 섬에서 BFS로 바다를 따라 다리 놓기
def find_shortest_bridge():
    dist = [[-1] * n for _ in range(n)]
    queue = deque()

    # 시작점: 모든 섬의 육지에서 시작
    for i in range(n):
        for j in range(n):
            if graph[i][j] > 1:
                dist[i][j] = 0
                queue.append((i, j))

    min_bridge = int(1e9)

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                # 바다라면 계속 확장
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y]  # 같은 섬 번호로 확장
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
                # 다른 섬을 만났다면 다리 길이 계산
                elif graph[nx][ny] != graph[x][y]:
                    min_bridge = min(min_bridge, dist[x][y] + dist[nx][ny])

    return min_bridge


# 실행
label_islands()
result = find_shortest_bridge()
print(result)