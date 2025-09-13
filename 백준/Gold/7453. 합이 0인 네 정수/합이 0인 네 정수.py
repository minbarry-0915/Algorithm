import sys
n = int(input())

A,B,C,D = [],[],[],[]

for _ in range(n):
    a,b,c,d = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB_sum = [a + b for a in A for b in B]
CD_sum = [c + d for c in C for d in D]

AB_sum.sort()
CD_sum.sort()

result = 0
left, right = 0, len(CD_sum) - 1

while left < len(AB_sum) and right >= 0:
    _sum = AB_sum[left] + CD_sum[right]
    if _sum == 0:
        a_val, b_val = AB_sum[left], CD_sum[right]
        a_cnt, b_cnt = 0,0
        while left < len(AB_sum) and AB_sum[left] == a_val:
            a_cnt += 1
            left += 1
        while right >= 0 and CD_sum[right] == b_val:
            b_cnt += 1
            right -= 1
        result += a_cnt * b_cnt
    elif _sum < 0:
        left += 1
    else:
        right -= 1

print(result)