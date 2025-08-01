def can_process(time, times, m):
    total = 0
    for t in times:
        total += time // t
    return total >= m


n,m = map(int,input().split())
times = [int(input()) for _ in range(n)]

left = 1
right = max(times) * m

answer = right

while left <= right:
    mid = (left + right) // 2
    if can_process(mid, times, m):
        answer = mid
        right = mid - 1
    else:
        left = mid + 1
print(answer)
