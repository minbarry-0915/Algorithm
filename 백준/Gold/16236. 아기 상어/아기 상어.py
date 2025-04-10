import sys
from collections import deque

#sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
fish_position = []
shark_position = ()
for i in range(n):
    for j in range(n):
        if 1 <= grid[i][j] <= 6:
            fish_position.append((i, j))
        if grid[i][j] == 9:
            shark_position = (i, j)
# 0 빈칸
# 1 ~ 6 물고기의 크기
# 9 상어의 위치

# 상어 위치 기준 물고기까지의 최단 거리 계산
# 제일 짧은 거리의 물고기 잡아먹고 grid 업데이트
# 잡아먹은 물고기 수 기반 상어 크기 업데이트
# 더이상 잡아먹을 물고기가 없으면, break
shark_size = 2

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(start_x, start_y, grid):
    visited = [[-1] * n for _ in range(n)]
    visited[start_x][start_y] = 0
    queue = deque([(start_x, start_y)])

    while queue:
        cx, cy = queue.popleft()
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 > nx or nx >= n or 0 > ny or ny >= n:
                continue
            if visited[nx][ny] == -1 and grid[nx][ny] <= shark_size:
                visited[nx][ny] = visited[cx][cy] + 1
                queue.append((nx, ny))
    return visited


def choose_fish():
    visited = bfs(shark_position[0], shark_position[1], grid)
    fish_distance = []

    for fx, fy in fish_position:
        if grid[fx][fy] != 0 and grid[fx][fy] < shark_size:
            distance = visited[fx][fy]
            if distance != -1:  # 방문할수 없는 위치가 아니면
                fish_distance.append((distance, fx, fy))

    if not fish_distance:
        return None

    fish_distance.sort()  # 거리 > 위 > 왼 순으로 정렬
    return fish_distance[0]

count = 0
time = 0

while True:
    fish = choose_fish()
    if fish is None:
        break
    distance, fish_x, fish_y = fish
    time += distance  # 거리만큼 시간이 걸림

    grid[shark_position[0]][shark_position[1]] = 0  # 원래 자리는 비우고
    shark_position = (fish_x, fish_y)  # 먹은 물고기 자리로 현재 상어 위치 저장
    grid[fish_x][fish_y] = 9  # 먹은 물고기 자리로 이동

    fish_position.remove((fish_x, fish_y))
    count += 1

    if count == shark_size:
        shark_size += 1
        count = 0  # 카운트 초기화

print(time)