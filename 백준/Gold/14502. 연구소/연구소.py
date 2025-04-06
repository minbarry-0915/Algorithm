# 벽 3개 세우고, bfs로 바이러스 퍼트리고, 안전지역 갯수 세고
import copy
import sys

input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

empty = [(i, j) for i in range(n) for j in range(m) if graph[i][j] == 0]
virus = [(i, j) for i in range(n) for j in range(m) if graph[i][j] == 2]
answer = 0


# 0: 빈칸, 1: 벽, 2: 바이러스
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


def makewall(start,cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(start, len(empty)):
        x, y = empty[i]
        graph[x][y] = 1
        makewall(i + 1, cnt + 1)
        graph[x][y] = 0


makewall(0,0)
print(answer)
