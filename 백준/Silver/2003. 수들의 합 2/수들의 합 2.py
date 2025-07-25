n, m = map(int,input().split())
lst = list(map(int,input().split()))

answer = 0
start = 0
end = 0
total = 0

while True:
    if total == m:
        answer += 1

    if total >= m:
        total -= lst[start]
        start += 1
    elif end == n:
        break
    else:
        total += lst[end]
        end += 1
print(answer)