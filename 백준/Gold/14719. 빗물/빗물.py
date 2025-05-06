import sys
# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())
heights = list(map(int, input().split()))

count = 0
for i in range(1, m - 1):
    ch = heights[i]
    left_max = max(heights[:i])
    right_max = max(heights[i + 1:])
    m = min(left_max, right_max)
    if m > ch:
        count += m - ch
print(count)