import sys
input = sys.stdin.readline

x, y = map(int, input().split())
z = (y * 100) // x

low, high = 0, 10**9
result = -1

while low <= high:
  mid = (low + high) // 2
  new_z = ((y + mid) * 100) // (x + mid)
  
  if new_z > z:
    result = mid
    high = mid - 1
  else:
    low = mid + 1
    
print(result)