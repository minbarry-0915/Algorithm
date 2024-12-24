N = int(input())  # N을 입력받습니다.

# 상단 부분
for i in range(1, N + 1):
    print(' ' * (N - i) + '*' * (2 * i - 1))

# 하단 부분
for i in range(N - 1, 0, -1):
    print(' ' * (N - i) + '*' * (2 * i - 1))