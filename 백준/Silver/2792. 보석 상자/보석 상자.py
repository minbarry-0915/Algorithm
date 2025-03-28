import sys
import math

input = sys.stdin.readline


n,m = map(int, input().split())
jewels = [int(input()) for _ in range(m)]

left, right = 1, max(jewels)
answer = right

while left <= right:
    mid = (left + right) // 2
    count = 0

    for jewel in jewels:
        count += math.ceil(jewel / mid)

    if count > n:
        left = mid + 1
    else:
        answer = mid
        right = mid - 1

print(answer)

