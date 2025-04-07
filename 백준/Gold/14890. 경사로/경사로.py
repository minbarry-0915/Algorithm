import sys

input = sys.stdin.readline

n, l = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
count = 0


def check_available(row):
    visited = [False] * n  # 경사로 있음 표현용

    for i in range(n - 1):
        if row[i] == row[i + 1]:  # 같을 경우: 경사로 검사 필요 없음
            continue

        elif row[i] == row[i + 1] + 1:  # 1 차이 나면
            for j in range(1, l + 1):
                # 경사로를 깔아야되는데 범위를 벗어났거나
                # 경사로를 깔아야되는 범위의 값이 같지 않거나
                # 이미 경사로를 깔았을 경우
                if i + j >= n or row[i + 1] != row[i + j] or visited[i + j]:
                    return False
            # 경사로 깔기
            for j in range(1, l + 1):
                visited[i + j] = True
        elif row[i] == row[i + 1] - 1:  # 높아 지는 경우
            # i 부터 까는 거임
            for j in range(l):
                # 경사로를 깔아야되는 범위가 벗어나거나
                # 경사로를 깔아야되는 범위의 값이 같지 않거나
                # 이미 경사로가 깔았을 경우
                if i - j < 0 or row[i] != row[i - j] or visited[i - j]:
                    return False

            # 경사로 깔기
            for j in range(l):
                visited[i - j] = True
        else:
            return False
    return True


# 행 검사
for row in maps:
    if check_available(row):
        count += 1

# 열 검사
for i in range(n):
    col = []
    for j in range(n):
        col.append(maps[j][i])
    if check_available(col):
        count += 1

print(count)
