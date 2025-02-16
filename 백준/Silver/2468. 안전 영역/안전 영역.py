import sys
sys.setrecursionlimit(10 * 6)
input = sys.stdin.readline
from collections import deque

def bfs(x,y, height, visited, grid, n):
    queue = deque([(x,y)])
    visited[x][y] = True
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx = cx + dx
            ny = cy + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and grid[nx][ny] > height:
                visited[nx][ny] = True
                queue.append((nx, ny))

def find_safe_area(grid, n, height):
    visited = [[False] * n for _ in range(n)]
    safe_area_count = 0

    for i in range(n):
        for j in range(n):
            if grid[i][j] > height and not visited[i][j]:
                bfs(i,j,height, visited, grid, n)
                safe_area_count += 1
    return safe_area_count



n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

max_safe_area = 0
max_height = max(map(max, grid))

for height in range(max_height + 1):
    max_safe_area = max(max_safe_area,find_safe_area(grid, n, height))

print(max_safe_area)