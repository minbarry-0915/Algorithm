n,h = map(int,input().split())
down = []
up = []

for i in range(n):
  x = int(input())
  if i % 2 == 0:
    down.append(x)
  else:
    up.append(x)

down.sort()
up.sort()

min_destroy = n #최악의 경우: 다 파괴
count = 0

def lower_bound(arr,x):
  left, right = 0, len(arr)
  while left < right:
    mid = (left + right) // 2
    if arr[mid] < x:
      left = mid + 1
    else:
      right = mid
  return left

for height in range(1, h + 1):
  destroy_down = len(down) - lower_bound(down, height)
  destroy_up = len(up) - lower_bound(up, h - height + 1)
  
  total = destroy_down + destroy_up
  
  if total < min_destroy:
    min_destroy = total
    count = 1
  elif total == min_destroy:
    count += 1

print(min_destroy, count)