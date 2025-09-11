import sys

n = int(input())
arr = list(map(int,input().split()))
arr.sort()

min_diff = float('inf')
ans = (0,0,0)

for i in range(n - 2):
  left, right = i + 1, n - 1
  
  while left < right:
    total = arr[i] + arr[left] + arr[right]
    if abs(total) < min_diff:
      min_diff = abs(total)
      ans = (arr[i],arr[left], arr[right])
      
    if total > 0:
      right -= 1
    elif total < 0:
      left += 1
    else:
      print(arr[i], arr[left],arr[right])
      sys.exit()
      
print(ans[0],ans[1],ans[2])
