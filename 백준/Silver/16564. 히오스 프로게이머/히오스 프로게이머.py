
n,k = map(int,input().split())
levels = [int(input()) for _ in range(n)]

start = min(levels)
end = min(levels) + k
res = -1
while start <= end:
    mid = (start + end) // 2

    total = 0
    for level in levels:
        diff = mid - level
        if diff > 0:
            total += diff

    if total <= k:
        start = mid + 1
        res = mid
    else:
        end = mid - 1
print(res)

