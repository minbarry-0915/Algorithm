import sys

# sys.stdin = open('input.txt', 'r', encoding='utf-8')

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(min_val, max_val):
    if not (min_val <= grid[0][0] <= max_val):
        return False

    visited = [[False] * n for _ in range(n)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = True

    while q:
        x, y = q.popleft()
        if x == n - 1 and y == n - 1:
            return True

        for d in range(4):
            nx,ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if min_val <= grid[nx][ny] <= max_val:
                    visited[nx][ny] = True
                    q.append((nx,ny))
    return False

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
min_val, max_val = 0, 200  # 차이값의 경계
answer = 0

while min_val <= max_val:
    mid = (min_val + max_val) // 2
    possible = False
    for start in range(0, 201 - mid):
        if bfs(start, start + mid):  # 가능한 최솟값, 가능한 최대값
            possible = True
            break
    if possible:
        answer = mid
        max_val = mid - 1 # 더 작은 값도 가능한지 확인하러 좌측으로 이동
    else:
        min_val = mid + 1

print(answer)