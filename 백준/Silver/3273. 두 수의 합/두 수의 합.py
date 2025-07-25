n = int(input())
lst = list(map(int,input().split()))
lst.sort()
x = int(input())


start = 0
end = n - 1
answer = 0

while start < end:
    total = lst[start] + lst[end]

    if total == x:
        answer += 1

    if total >= x:
        end -= 1
    else:
        start += 1
print(answer)