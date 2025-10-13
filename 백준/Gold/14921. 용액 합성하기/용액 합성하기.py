
n = int(input())
arr = list(map(int,input().split()))
left = 0
right = n - 1
min_diff = int(1e9)
answer = 0
while left < right:
    total = arr[left] + arr[right]
    diff = abs(total)

    if diff < min_diff:
        min_diff = diff
        answer = total

    if total < 0:
        left += 1
    else:
        right -= 1

print(answer)