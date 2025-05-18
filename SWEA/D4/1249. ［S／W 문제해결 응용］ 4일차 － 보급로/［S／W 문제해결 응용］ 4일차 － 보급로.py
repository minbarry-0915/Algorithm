import heapq
# import sys

# sys.stdin = open('input.txt', 'r', encoding='UTF-8')

# 방법 1. 우선 순위 큐(BFS)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

INF = int(1e9)
from collections import deque


def bfs(n, grid):
    dist = [[INF] * n for _ in range(n)]
    dist[0][0] = 0

    # 방법 1. 우선 순위 큐(BFS)
    # q = deque()
    # q.append((0, 0))
    #
    # while q:
    #     x, y = q.popleft()
    #     for d in range(4):
    #         nx, ny = x + dx[d], y + dy[d]
    #         if 0 <= nx < n and 0 <= ny < n:
    #             cost = dist[x][y] + grid[nx][ny]
    #             if cost < dist[nx][ny]:
    #                 dist[nx][ny] = cost
    #                 q.append((nx, ny))

    # 방법 2. 다익스트라
    q = []
    heapq.heappush(q, (0, 0, 0))

    while q:
        cost, x, y = heapq.heappop(q)

        if dist[x][y] < cost:
            continue

        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n:
                new_cost = cost + grid[nx][ny]
                if new_cost < dist[nx][ny]:
                    dist[nx][ny] = new_cost
                    heapq.heappush(q, (new_cost, nx, ny))
    return dist[n - 1][n - 1]


T = int(input())
for t in range(1, T + 1):
    n = int(input())
    grid = [list(map(int, input().strip())) for _ in range(n)]
    print(f'#{t} {bfs(n, grid)}')
