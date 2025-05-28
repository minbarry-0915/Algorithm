import sys

# sys.stdin = open('input.txt', 'r', encoding='utf-8')
input = sys.stdin.readline
T = int(input())
for t in range(1, T + 1):
    k = int(input())
    files = list(map(int, input().split()))

    s_lst = [0] * (k + 1)
    for i in range(k):
        s_lst[i + 1] = s_lst[i] + files[i]

    dp = [[0] * (k + 1) for _ in range(k + 1)]

    for l in range(2, k + 1):
        for i in range(1, k - l + 2):
            j = i + l - 1
            dp[i][j] = float('inf')
            for m in range(i,j):
                cost = dp[i][m] + dp[m + 1][j] + s_lst[j] - s_lst[i - 1]
                dp[i][j] = min(dp[i][j], cost)
    print(dp[1][k])