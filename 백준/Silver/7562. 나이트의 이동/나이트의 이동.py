#나이트의 이동 - BFS
import sys
sys.setrecursionlimit(10 * 6)
input = sys.stdin.readline
from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(l, start, end):
    queue = deque([start])
    visited = [[-1] * l for _ in range(l)]
    visited[start[0]][start[1]] = 0

    while queue:
        x,y = queue.popleft()
        
        if (x,y) == end:
            return visited[x][y]
        
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

t = int(input())
for _ in range(t):
    l = int(input())
    start = tuple(map(int, input().split()))
    end = tuple(map(int, input().split()))
    print(bfs(l, start, end))
