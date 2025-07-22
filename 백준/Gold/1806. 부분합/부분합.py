import sys

# sys.stdin = open('input.txt', 'r', encoding='utf-8')

n, s = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 0
total = 0
answer = int(1e9)

while True:
    if total >= s:
        answer = min(answer, right - left)
        total -= arr[left]
        left += 1
    elif right == n:
        break
    else:
        total += arr[right]
        right += 1

print(answer if answer != int(1e9) else 0)
