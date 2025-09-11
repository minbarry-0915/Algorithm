T = int(input())
n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

a_sum = []
for i in range(n):
  s = 0
  for j in range(i, n):
    s += a[j]
    a_sum.append(s)

b_sum = []
for i in range(m):
  s = 0
  for j in range(i,m):
    s += b[j]
    b_sum.append(s)
    
from collections import Counter
b_counter = Counter(b_sum)
answer = 0
for x in a_sum:
  answer += b_counter[T - x]
print(answer)