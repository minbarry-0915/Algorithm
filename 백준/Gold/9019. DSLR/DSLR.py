import sys
#sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
from collections import deque
t = int(input())
for _ in range(t):
    start, target = map(int, input().split())
    visited = [False] * 10001

    queue = deque()
    queue.append([start, ''])
    visited[start] = True

    while queue:
        x, cmd = queue.popleft()

        if x == target:
            print(cmd)
            break

        d = (x * 2) % 10000
        if not visited[d]:
            visited[d] = True
            queue.append([d, cmd + 'D'])

        s = (x - 1) % 10000
        if not visited[s]:
            visited[s] = True
            queue.append([s, cmd + 'S'])

        l = x // 1000 + (x % 1000) * 10
        if not visited[l]:
            visited[l] = True
            queue.append([l, cmd + 'L'])

        r = x // 10 + (x % 10) * 1000
        if not visited[r]:
            visited[r] = True
            queue.append([r, cmd + 'R'])