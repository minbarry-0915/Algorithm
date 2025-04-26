import sys

#sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())
teleport = dict()

for _ in range(n):
    start, end = map(int, input().split())
    teleport[start] = end
for _ in range(m):
    start, end = map(int, input().split())
    teleport[start] = end

visited = [0] * 101
from collections import deque

queue = deque()
queue.append(1)

while queue:
    x = queue.popleft()
    for dice in range(1, 7):
        nx = x + dice
        if nx > 100:
            continue
        if nx in teleport:
            nx = teleport[nx]
        if visited[nx] == 0:
            visited[nx] = visited[x] + 1
            queue.append(nx)

print(visited[100])