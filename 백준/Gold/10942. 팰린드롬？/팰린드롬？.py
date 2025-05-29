import sys

# sys.stdin = open('input.txt', 'r', encoding='utf-8')

input = sys.stdin.readline

n = int(input())
numbers = list(input().split())
m = int(input())
# 1. 시도
# questions = [tuple((map(int,input().split()))) for _ in range(m)]
#
# for start, end in questions:
#     query = ''.join(numbers[start - 1: end])
#
#     if query == query[::-1]:
#         print(1)
#     else:
#         print(0)

# 2. 정답
# 접근 : dp
dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1

for i in range(n - 1):
    if numbers[i] == numbers[i + 1]:
        dp[i][i + 1] = 1

for l in range(3, n + 1):
    for i in range(n - l + 1):
        j =  i + l - 1
        if numbers[i] == numbers[j] and dp[i + 1][j - 1]:
            dp[i][j] = 1

for _ in range(m):
    s, e = map(int,input().split())
    print(dp[s - 1][e - 1])