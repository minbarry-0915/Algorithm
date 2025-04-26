import sys
from collections import deque

#sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n, k = map(int, input().split())
max_size = 100001
visited = [-1] * max_size  # -1이면 방문 안 한 것
queue = deque()

queue.append(n)
visited[n] = 0

while queue:
    x = queue.popleft()
    if x == k:
        break
    for nx in (x * 2, x - 1, x + 1): # 순간이동의 우선순위가 더 높음
        if 0 <= nx < 100001 and visited[nx] == -1:
            if nx == x * 2:
                visited[nx] = visited[x]
                queue.appendleft(nx) # 큐의 앞에 삽입
            else:
                visited[nx] = visited[x] + 1
                queue.append(nx)
print(visited[k])
