import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(int(input()) for _ in range(n))

low, high = max(numbers), sum(numbers)
result = high

while low <= high:
  mid = (low + high) // 2
  count = 1
  money = mid

  for cost in numbers:
    if money < cost: #작으면 인출 다시해야됨
      count += 1
      money = mid
    money -= cost

  if count > m:
    low = mid + 1
  else:
    result = mid
    high = mid - 1

print(result)