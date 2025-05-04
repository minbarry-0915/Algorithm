import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

from collections import deque


def bfs():
    queue = deque()
    queue.append((0, 0, 0))
    visited[0][0][0] = 1

    while queue:
        cx, cy, cnt = queue.popleft()

        if cx == n - 1 and cy == m - 1:
            return visited[cx][cy][cnt]

        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]

            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == 1 and cnt == 0 and visited[nx][ny][1] == 0:  # 다음지점이 벽인데 방문안하고 부숨
                    visited[nx][ny][1] = visited[cx][cy][0] + 1
                    queue.append((nx, ny, 1))
                elif grid[nx][ny] == 0 and visited[nx][ny][cnt] == 0:  # 다음지점이 벽이 아닌데 방문안함
                    visited[nx][ny][cnt] = visited[cx][cy][cnt] + 1
                    queue.append((nx, ny, cnt))
    return - 1


n, m = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

print(bfs())
