import sys
input = sys.stdin.readline

def binary_search(arr, target):
  low, high = 0, len(arr) - 1
  while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
      return 1
    elif arr[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  return 0


t = int(input())
for _ in range(t):
  n = int(input())
  n_num = list(map(int, input().split()))
  m = int(input())
  m_num = list(map(int, input().split()))
  n_num.sort()
  
  result =[binary_search(n_num, num) for num in m_num]
  print("\n".join(map(str, result)))