import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
m = int(input())

numbers.sort()

low, high = 0, max(numbers)
result = 0

while low <= high:
  mid = (low + high) // 2
  total = sum(min(num, mid) for num in numbers)
  
  if total <= m:
    result = mid
    low = mid + 1
  else:
    high = mid - 1

print(result)