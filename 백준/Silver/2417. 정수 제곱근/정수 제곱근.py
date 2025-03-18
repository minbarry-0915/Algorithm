import sys
input = sys.stdin.readline

n = int(input())

low, high = 0, n
while low <= high:
  mid = (low + high) // 2
  if mid * mid >= n:
    high = mid - 1
  else:
    low = mid + 1
    
print(low)