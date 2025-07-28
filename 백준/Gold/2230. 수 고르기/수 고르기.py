import sys

# sys.stdin = open('input.txt', 'r', encoding='utf-8')
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

start = 0
end = 0
min_diff = int(2e9)

while start < n and end < n:
    diff = arr[end] - arr[start]

    if diff < m:
        end += 1
    else:
        min_diff = min(min_diff, diff)
        start += 1

print(min_diff)
