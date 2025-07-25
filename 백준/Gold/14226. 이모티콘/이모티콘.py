s = int(input())

from collections import deque
queue = deque()
visited = [[-1] * 1001 for _ in range(1001)]

queue.append((1,0))
visited[1][0] = 0

while queue:
    screen, clipboard = queue.popleft()

    if screen == s:
        print(visited[screen][clipboard])
        break

    # 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
    if visited[screen][screen] == -1:
        visited[screen][screen] = visited[screen][clipboard] + 1
        queue.append((screen, screen))

    # 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
    if clipboard > 0 and screen + clipboard < 1001 and visited[screen + clipboard][clipboard] == -1:
        visited[screen + clipboard][clipboard] = visited[screen][clipboard] + 1
        queue.append((screen + clipboard, clipboard))

    # 화면에 있는 이모티콘 중 하나를 삭제한다.
    if screen > 0 and visited[screen - 1][clipboard] == -1:
        visited[screen - 1][clipboard] = visited[screen][clipboard] + 1
        queue.append((screen - 1, clipboard))