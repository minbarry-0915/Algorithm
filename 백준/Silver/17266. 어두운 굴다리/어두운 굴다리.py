import sys
from operator import truediv

input = sys.stdin.readline

n = int(input())
m = int(input())
positions = list(map(int, input().split()))

left,right = 1, n
answer = n

while left <= right:
     mid = (left + right) // 2
     current = 0
     possible = True
     
     for pos in positions:
         if pos - mid > current:
             possible = False
             break
         current = pos + mid
     
     if current < n:
         possible = False
         
     if possible:
         answer = mid
         right = mid - 1
     else:
         left = mid + 1
         
print(answer)
    