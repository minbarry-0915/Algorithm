n, c = map(int, input().split())
houses = list(int(input()) for _ in range(n))
houses.sort()

left = 1
right = houses[-1] - houses[0]
answer = 0


def is_possible(dist):
    count = 1
    last = houses[0]
    for i in range(1, n):
        if houses[i] - last >= dist:
            count += 1
            last = houses[i]
    return count >= c

while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)