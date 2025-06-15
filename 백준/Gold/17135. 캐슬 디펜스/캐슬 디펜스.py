import sys

# sys.stdin = open('input.txt','r')
from collections import deque

def bfs(x, y):
    queue = deque()
    visited = [[False] * m for _ in range(n)]
    queue.append((x, y, 1))  # (현재 x, y, 거리)
    visited[x][y] = True
    candidates = []
    while queue:
        cx, cy, dist = queue.popleft()
        if dist > d:
            break

        # 적을 찾으면 바로 리턴
        if grid_copy[cx][cy] == 1:
            candidates.append((dist, cy, cx))

        for dx_, dy_ in [(-1, 0), (0, -1), (0, 1)]:  # 바로위,왼쪽,오른쪽
            nx, ny = cx + dx_, cy + dy_
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))

    if candidates:
        candidates.sort()  # 거리, 열 순
        _, ey, ex = candidates[0]
        return ex, ey
    else:
        return -1, -1

        
def simulation(archers):
    enemy_set = set()
    cnt = 0

    for x in range(n - 1, -1,-1): # 아처 바로 위
        enemy_set.clear()
        for y in archers:
            # 아처위치 기준 최적의 적 고름
            ex,ey = bfs(x,y)
            if ex != -1 and ey != -1 and (ex,ey) not in enemy_set:
                enemy_set.add((ex,ey))

        for ex, ey in enemy_set:
            if grid_copy[ex][ey] == 1:
                grid_copy[ex][ey] = 0

        cnt += len(enemy_set)

    return cnt


n,m, d = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
grid_copy = [row[:] for row in grid] # 백트랙킹용으로 복사
ans = -1
from itertools import combinations 
for archers in combinations(range(m), 3): # 아처가 있을수있는 위치 계산

    ans = max(ans, simulation(archers))
    grid_copy = [row[:] for row in grid]
print(ans)