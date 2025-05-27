import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

T = int(input())
for t in range(1, T + 1):
    k = int(input())  # 파일 개수
    lst = list(map(int, input().split()))

    s_lst = [0] * (k + 1)
    for i in range(k):
        s_lst[i + 1] = s_lst[i] + lst[i]

    dp = [[0] * k for _ in range(k)]

    for l in range(2, k + 1):  # 구간 길이
        for i in range(k - l + 1):  # 시작 인덱스
            j = i + l - 1
            dp[i][j] = float('inf')

            for mid in range(i, j):  # 분할 지점
                cost = dp[i][mid] + dp[mid + 1][j] + s_lst[j + 1] - s_lst[i]
                dp[i][j] = min(dp[i][j], cost)

    print(dp[0][k - 1])
