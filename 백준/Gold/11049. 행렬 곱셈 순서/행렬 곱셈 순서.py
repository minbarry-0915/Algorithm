import sys

# sys.stdin = open('input.txt', 'r', encoding='utf-8')

input = sys.stdin.readline
n = int(input().strip())
matrix_lst = [tuple(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

for l in range(2, n + 1):
    for i in range(n - l + 1):
        j = i + l - 1
        dp[i][j] = float('inf')
        for k in range(i, j):
            cost = dp[i][k] + dp[k + 1][j] + matrix_lst[i][0] * matrix_lst[k][1] * matrix_lst[j][1]
            dp[i][j] = min(dp[i][j], cost)
print(dp[0][n - 1])