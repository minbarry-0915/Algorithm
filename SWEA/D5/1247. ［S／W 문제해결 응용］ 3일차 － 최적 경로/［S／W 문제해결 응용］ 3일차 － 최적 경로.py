# import sys
from collections import deque
import math
# sys.stdin = open('input.txt', 'r', encoding='utf-8')

def dfs(distance,x,y):

    if all(visited):
        global min_dist
        distance += abs(hx - x) + abs(hy - y) # 집으로 돌아가는 경로 더하기
        min_dist = min(min_dist,distance)
        return

    for i in range(n):
        nx,ny = cus_positions[i]
        if not visited[i]:
            visited[i] = True
            dist = abs(nx-x) + abs(ny - y)
            dfs(distance + dist, nx,ny)
            visited[i] = False

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    temp = list(map(int, input().split()))
    positions = [(temp[i], temp[i + 1]) for i in range(0, len(temp), 2)]

    visited = [False] * n

    cx, cy = positions[0]  # 회사
    hx, hy = positions[1]  # 집
    cus_positions = positions[2:]  # 고객들
    min_dist = int(1e9)
    dfs(0,cx,cy)
    print(f'#{t} {min_dist}')

