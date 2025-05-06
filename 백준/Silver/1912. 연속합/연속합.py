import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
dp = lst[::]

if n == 1:
    print(dp[0])
else:
    for i in range(1, n):
        dp[i] = max(dp[i], dp[i - 1] + lst[i])
    print(max(dp))