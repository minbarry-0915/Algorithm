
n = int(input())
lst = list(map(int,input().split()))

# O(n^2)
# dp = [0] * n
#
# dp[0] = 1
# for i in range(1, n):
#     for j in range(i):
#         if lst[i] > lst[j]:
#             dp[i] = max(dp[i], dp[j] + 1)
# print(max(dp))

# 이분탐색 O(nlogn)
import bisect

dp = []

for num in lst:
    idx = bisect.bisect_left(dp, num)
    if idx == len(dp):
        dp.append(num)
    else:
        dp[idx] = num

print(len(dp))