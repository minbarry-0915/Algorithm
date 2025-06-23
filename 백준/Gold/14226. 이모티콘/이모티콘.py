
from collections import deque

s = int(input())
MAX = 1001

visited = [[-1] * MAX for _ in range(MAX)]
queue = deque()

queue.append((1,0))
visited[1][0] = 0

while queue:
    screen, clipboard = queue.popleft()

    if screen == s:
        print(visited[screen][clipboard])
        break

    if visited[screen][screen] == -1:
        visited[screen][screen] = visited[screen][clipboard] + 1
        queue.append((screen,screen))

    if clipboard > 0 and screen + clipboard < MAX and visited[screen + clipboard][clipboard] == -1:
        visited[screen + clipboard][clipboard] = visited[screen][clipboard] + 1
        queue.append((screen + clipboard, clipboard))

    if screen - 1 >= 0 and visited[screen - 1][clipboard] == -1:
        visited[screen - 1][clipboard] = visited[screen][clipboard] + 1
        queue.append((screen - 1, clipboard))