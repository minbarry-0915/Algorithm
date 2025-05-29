import sys

# sys.stdin = open('input.txt', 'r', encoding='utf-8')

input = sys.stdin.readline

from collections import deque
from itertools import permutations

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(start, board, n, m):
    x, y = start
    visited = [[-1] * m for _ in range(n)]
    visited[x][y] = 0
    queue = deque()
    queue.append((x, y))

    while queue:
        cx, cy = queue.popleft()

        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1 and board[nx][ny] != 'x':
                visited[nx][ny] = visited[cx][cy] + 1
                queue.append((nx, ny))
    return visited


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    board = []
    points = []  # 더러운 칸들 + 시작 위치
    for i in range(h):
        row = list(input().strip())
        for j in range(w):
            if row[j] == 'o':
                points.insert(0, (i, j))  # 시작 위치를 맨 앞에 삽입
            elif row[j] == '*':
                points.append((i, j))
        board.append(row)

    n = len(points)
    dist = [[-1] * n for _ in range(n)]
    flag = False

    # 모든 점 사이 거리 계산
    for i in range(n):
        visited = bfs(points[i], board, h, w) #해당 점 기준 다른 포인트들까지의 최소 거리 획득
        for j in range(n):
            if i == j: # 같은애는 필요없음
                continue
            x, y = points[j]
            dist[i][j] = visited[x][y]
            if dist[i][j] == -1:
                flag = True  # 접근 불가능한 경우

    if flag:
        print(-1)
        continue

    # 순열로 최소 거리 찾기
    min_dist = float('inf')
    for order in permutations(range(1, n)):  # 시작점 제외하고 순열 ex) (1,2,3,4), (1,3,2,4) 
        d = dist[0][order[0]]
        for i in range(len(order) - 1):
            d += dist[order[i]][order[i + 1]]
        min_dist = min(min_dist, d)

    print(min_dist)