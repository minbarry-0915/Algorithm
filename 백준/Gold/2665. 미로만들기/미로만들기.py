from collections import deque

n = int(input())
grid = [list(input().strip()) for _ in range(n)]

# 최소 벽 부순 횟수 기록
visited = [[-1] * n for _ in range(n)]
visited[0][0] = 0

queue = deque()
queue.append((0, 0))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            cost = visited[x][y]
            if grid[nx][ny] == '0': # 검은방
                cost += 1

            if visited[nx][ny] == -1 or visited[nx][ny] > cost:
                visited[nx][ny] = cost
                if grid[nx][ny] == '0': # 검은방
                    queue.append((nx, ny))       # 비용 1 → 뒤에 넣음
                else:
                    queue.appendleft((nx, ny))  # 비용 0 → 앞에 넣음

print(visited[n-1][n-1])
