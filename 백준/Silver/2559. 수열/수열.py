import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))

window_sum = sum(lst[:k])
max_sum = window_sum

for i in range(k , n):
    window_sum += lst[i] - lst[i - k]
    max_sum = max(max_sum, window_sum)
print(max_sum)