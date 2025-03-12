import sys
input = sys.stdin.readline

m, n = map(int, input().split())
numbers = list(map(int, input().split()))

low, high = 1, max(numbers)
result = 0
while low <= high:
  mid = (low + high) // 2
  count = 0

  for number in numbers:
    if number < mid:
      continue
    else:
      count += number // mid

  if count >= m:
    result = mid
    low = mid + 1
  else:
    high = mid - 1

print(result)