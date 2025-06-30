
'''
접근: 이분 탐색 + 조합
'''

n = int(input())
lst = list(map(int, input().split()))
lst.sort()

left = 0
right = n - 1
ans = (lst[left], lst[right])
min_val = abs(lst[left] + lst[right])


while left < right:
    total = lst[left] + lst[right]
    if abs(total) < min_val:
        min_val = abs(total)
        ans = (lst[left],lst[right])

    if total == 0:
        break
    elif total < 0:
        left += 1
    else:
        right -= 1

print(ans[0], ans[1])
