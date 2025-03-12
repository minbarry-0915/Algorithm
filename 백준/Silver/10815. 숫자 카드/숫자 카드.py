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

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

cards.sort()
result = [binary_search(cards, target) for target in targets]
print(*result)