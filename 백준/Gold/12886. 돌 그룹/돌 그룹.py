

a,b,c = map(int,input().split())

from collections import deque

def bfs(a,b,c):
    total = a + b + c
    visited = [[False] * 1501 for _ in range(1501)]

    queue = deque()
    queue.append((a,b))
    visited[a][b] = True

    while queue:
        x,y = queue.popleft()
        z = total - x - y
        if x == y == z:
            return 1

        for a,b in((x,y),(x,z),(y,z)):
            if a != b:
                small = min(a,b)
                big = max(a,b)
                c = total - a - b

                nxt = sorted([small * 2, big - small, c])
                nx,ny = nxt[0], nxt[1]
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx,ny))
    return 0

print(bfs(a,b,c))