import sys
import copy
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

empty = [(i, j) for i in range(n) for j in range(m) if graph[i][j] == 0]
virus = [(i, j) for i in range(n) for j in range(m) if graph[i][j] == 2]

answer = 0


def bfs():
    tmp_graph = copy.deepcopy(graph)
    queue = deque(virus)

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if tmp_graph[nx][ny] == 0:
                    tmp_graph[nx][ny] = 2
                    queue.append((nx, ny))

    global answer
    section = sum(row.count(0) for row in tmp_graph)
    answer = max(answer, section)


def dfs_wall(start, count):
    if count == 3:
        bfs()
        return

    for i in range(start, len(empty)):
        x, y = empty[i]
        graph[x][y] = 1
        dfs_wall(i + 1, count + 1)
        graph[x][y] = 0


dfs_wall(0, 0)
print(answer)
