import sys
# sys.stdin = open('input.txt','r', encoding='utf-8')
input = sys.stdin.readline

from collections import deque
from itertools import permutations

n = int(input())
scv = list(map(int,input().split()))
scv += [0] * (3 - n)

queue = deque()
visited = [[[-1] * 61 for _ in range(61)] for _ in range(61)]

queue.append((scv[0],scv[1],scv[2]))
visited[scv[0]][scv[1]][scv[2]] = 0

while queue:
    current = queue.popleft()

    if current == (0,0,0):
        print(visited[current[0]][current[1]][current[2]])
        break
    for case in permutations([9,3,1],3):
        t = (max(current[0] - case[0],0), max(current[1]- case[1],0), max(current[2] - case[2], 0))

        if visited[t[0]][t[1]][t[2]] == -1:
            visited[t[0]][t[1]][t[2]] = visited[current[0]][current[1]][current[2]] + 1
            queue.append(t)
