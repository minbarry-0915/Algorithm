import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

r, c, t = map(int, input().split())  # 행, 열, 제한 시간
grid = [[0] * c for _ in range(r)]  # r * c 지도
dust_info = []  # 미세먼지 위치, 양
air_conditioner_position = []  # 공기청정기 현재 위치
grid_for_dust_calculation = [[0] * c for _ in range(r)]  # 매시간 마다 미세먼지 변화량 저장용

# 동남서북(시계 방향)
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# 그리드 정보 입력
for i in range(r):
    row = list(map(int, input().split()))
    for j in range(c):
        if row[j] != 0:
            if row[j] == -1:  # 공기청정기 위치
                air_conditioner_position.append((i, j))
            else:  # 미세먼지 위치
                dust_info.append((i, j, row[j]))
        grid[i][j] = row[j]


# 미세먼지 확산 그리드 계산
def calculate_dust():
    global grid
    temp = [[0] * c for _ in range(r)]

    for x in range(r):
        for y in range(c):
            if grid[x][y] > 0:
                spread_amount = grid[x][y] // 5
                if spread_amount == 0:
                    continue
                count = 0
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if not (0 <= nx < r and 0 <= ny < c):
                        continue
                    if grid[nx][ny] == -1:
                        continue
                    temp[nx][ny] += spread_amount
                    count += 1
                grid[x][y] -= spread_amount * count

    # 확산된 값 합치기
    for i in range(r):
        for j in range(c):
            grid[i][j] += temp[i][j]


# 공기청정기 청소
def clean():
    upper_x, upper_y = -1, 0  # 공기청정기 위 부분 인덱스
    lower_x, lower_y = -1, 0  # 공기청정기 아래 부분 인덱스
    air_conditioner_position.sort()  # x 정렬
    upper_x = air_conditioner_position[0][0]
    lower_x = air_conditioner_position[1][0]

    # 위쪽 - 반시계 방향
    for i in range(upper_x - 1, 0, -1):  # 아래 → 위
        grid[i][0] = grid[i - 1][0]
    for i in range(c - 1):  # 왼쪽 → 오른쪽
        grid[0][i] = grid[0][i + 1]
    for i in range(upper_x):  # 위 → 아래
        grid[i][c - 1] = grid[i + 1][c - 1]
    for i in range(c - 1, 1, -1):  # 오른쪽 → 왼쪽
        grid[upper_x][i] = grid[upper_x][i - 1]
    grid[upper_x][1] = 0  # 공기청정기에서 바람 나옴

    # 아래쪽 - 시계 방향
    for i in range(lower_x + 1, r - 1):  # 위 → 아래
        grid[i][0] = grid[i + 1][0]
    for i in range(c - 1):  # 왼쪽 → 오른쪽
        grid[r - 1][i] = grid[r - 1][i + 1]
    for i in range(r - 1, lower_x, -1):  # 아래 → 위
        grid[i][c - 1] = grid[i - 1][c - 1]
    for i in range(c - 1, 1, -1):  # 오른쪽 → 왼쪽
        grid[lower_x][i] = grid[lower_x][i - 1]
    grid[lower_x][1] = 0  # 공기청정기에서 바람 나옴

# 시뮬레이션 실행
for _ in range(t):
    calculate_dust()
    clean()

# 결과 합산
total = 0
for i in range(r):
    for j in range(c):
        if grid[i][j] > 0:
            total += grid[i][j]

print(total)