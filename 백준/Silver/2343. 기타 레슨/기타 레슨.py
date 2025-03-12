import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lessons = list(map(int, input().split()))

low, high = max(lessons), sum(lessons)

while low <= high:
  mid = (low + high) // 2
  count = 1
  temp = 0

  for lesson in lessons:
    if temp + lesson > mid:
      count += 1
      temp = 0
    temp += lesson

  if count <= m:
    high = mid - 1
  else:
    low = mid + 1

print(low)