import sys
from collections import deque
input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())

def bfs(f, s, g):
    queue = deque()
    queue.append(s)
    visited = [-1] * (f + 1)
    visited[s] = 0  # 시작 위치 초기화!!!

    while queue:
        current = queue.popleft()

        if current == g:
            return visited[current]

        for option in [current + u, current - d]:
            if 1 <= option <= f and visited[option] == -1:
                visited[option] = visited[current] + 1
                queue.append(option)

    return "use the stairs"

print(bfs(f, s, g))
