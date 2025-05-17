# import sys
#sys.stdin = open('input.txt','r', encoding='UTF-8')

r,c = map(int,input().split())
grid = [list(input().strip()) for _ in range(r)]
n = int(input())
heights = list(map(int,input().split()))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

from collections import deque

def bfs(x,y,visited):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    cluster = [(x,y)]

    while q:
        cx,cy = q.popleft()
        for d in range(4):
            nx,ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and grid[nx][ny] == 'x':
                visited[nx][ny] = 1
                q.append((nx,ny))
                cluster.append((nx,ny))
    return cluster

def fall(cluster):
    for x,y in cluster:
        grid[x][y] = '.'

    fall_dist = r
    for x,y in cluster:
        nx = x + 1
        while nx < r and grid[nx][y] == '.':
            nx += 1
        fall_dist = min(fall_dist, nx - x - 1)

    for x, y in sorted(cluster, reverse=True):
        grid[x + fall_dist][y] = 'x'

for i in range(len(heights)):
    # 1. 미네랄 제거
    x = r - heights[i]
    if i % 2 == 0: # 왼쪽에서 오른쪽으로
        for j in range(c):
            if grid[x][j] == 'x': # 미네랄 제거
                grid[x][j] = '.'
                break
    else: # 오른쪽에서 왼쪽으로
        for j in range(c - 1, -1, -1):
            if grid[x][j] == 'x':
                grid[x][j] = '.'
                break

    # 2. 클러스터 탐색
    fall_happened = False
    visited = [[0] * c for _ in range(r)]
    for i in range(r - 1, -1, -1):
        for j in range(c):
            if grid[i][j] == 'x' and not visited[i][j]:
                cluster = bfs(i, j, visited)
                cluster.sort(reverse=True)

                is_bottom = any(x == r - 1 for x, y in cluster)
                if not is_bottom:
                    fall(cluster)
                    fall_happened = True
                    break
        if fall_happened:
            break

for row in grid:
    print(''.join(row))