
count = {-1: 0, 0: 0, 1: 0}
n = int(input()) # 3^k의 꼴
grid = [list(map(int, input().split())) for _ in range(n)]

# 분할정복, 재귀로 접근
# 서브 배열의 모든 값이 -1, 0, 1일 경우 -> 카운트 업데이트
# 아닐경우 n // 3의로 서브 배열 길이 결정 및 9개로 분할

def get_result(x, y, size):
    base = grid[x][y]
    not_same = False

    for i in range(x, x + size):
        for j in range(y, y + size):
            if grid[i][j] != base:
                not_same = True
                break
        if not_same:
            break

    if not not_same:
        count[base] += 1
        return
    else:
        sub_size = size // 3
        for i in range(x, x + size, sub_size):
            for j in range(y, y + size, sub_size):
                get_result(i, j, sub_size)
get_result(0,0,n)

print(count[-1])
print(count[0])
print(count[1])
