

# 접급 1. -> 시간초과
# n = int(input())
# u = list(int(input()) for _ in range(n))
# u.sort()
# from itertools import combinations
# cases = combinations(u, 3)
# cases = list(cases)
# left = 0
# right = len(cases) - 1
#
# d = 0
#
# while left <= right:
#     mid = (left + right) // 2
#     if sum(cases[mid]) in u:
#         d = sum(cases[mid])
#         left += 1
#     else:
#         right -= 1
# print(d)

# 접근 2. (블로그 참고)
'''
u[i] + u[i + 1] + u[i + 2] in u 
-> u[i] + u[i + 1] = u[?] - u[i + 2] 
'''
n = int(input())
u = [int(input()) for _ in range(n)]
u.sort()

cases = set()
for x in u:
    for y in u:
        cases.add(x + y)

def solve():
    # 뒤에서 부터 탐색해서 가장 큰 차이부터 찾음
    for i in range(n - 1, -1, -1):
        for j in range(i + 1):
            if u[i] - u[j] in cases:
                return u[i]
print(solve())