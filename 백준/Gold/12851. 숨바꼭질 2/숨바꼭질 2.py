import sys

# sys.stdin = open('input.txt', 'r', encoding='UTF-8')

n, k = map(int, input().split())
max_pos = 100001
visited = [-1 for _ in range(max_pos)]
count = [0 for _ in range(max_pos)]

from collections import deque

q = deque()
q.append(n)
visited[n] = 0
count[n] = 1

while q:
    now = q.popleft()
    for next_pos in [now - 1, now + 1, now * 2]:
        if 0 <= next_pos < max_pos:
            if visited[next_pos] == -1:
                visited[next_pos] = visited[now] + 1
                count[next_pos] = count[now]
                q.append(next_pos)
            elif visited[next_pos] == visited[now] + 1:
                count[next_pos] += count[now]
print(visited[k])
print(count[k])
