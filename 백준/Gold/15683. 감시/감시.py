import copy
import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())
office = []
cctvs = []

for i in range(n):
    row = list(map(int, input().split()))
    office.append(row)
    for j in range(m):
        if 1 <= office[i][j] <= 5:
            cctvs.append((office[i][j], i, j))  # cctv 번호, 행,열

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]  # 동남서북(시계방향)
moves = [
    [0],
    [[0], [1], [2], [3]],  # 1
    [[0, 2], [1, 3]],  # 2
    [[0, 1], [1, 2], [2, 3], [3, 0]],  # 3
    [[0, 1, 3], [0, 1, 2], [1, 2, 3], [0, 2, 3]],  # 4
    [[0, 1, 2, 3]]  # 5
]


def watch(i, j, office,move_set):
    for move in move_set:
        ny, nx = i, j
        while True:
            ny += dx[move]
            nx += dy[move]

            if not (0 <= nx < m and 0 <= ny < n):
                break
            if office[ny][nx] == 6:
                break
            if office[ny][nx] == 0:
                office[ny][nx] = -1


answer = int(1e9)
def dfs(depth, office):
    global answer
    if depth == len(cctvs):
        # 계산
        non_save_area = sum(row.count(0) for row in office)
        answer = min(answer, non_save_area)
        return

    temp_office = copy.deepcopy(office)
    cctv_num, i, j = cctvs[depth]
    for move_set in moves[cctv_num]:
        watch(i, j, temp_office, move_set)
        dfs(depth + 1, temp_office)
        temp_office = copy.deepcopy(office)


dfs(0, office)
print(answer)
