import sys
input = sys.stdin.readline
import bisect

t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  a_list = list(map(int, input().split()))
  b_list = list(map(int, input().split()))

  b_list.sort()
  # b에서 a보다 작은 숫자의 갯수를 세야됨
  result = 0
  for a in a_list:
    count = bisect.bisect_left(b_list, a)
    result += count
    
  print(result)