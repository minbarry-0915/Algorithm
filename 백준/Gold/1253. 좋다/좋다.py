n = int(input())
lst = list(map(int,input().split()))
lst.sort()

answer = 0
for i in range(n):
    temp = lst[:i] + lst[i + 1:]
    start, end = 0, len(temp) - 1

    while start < end:
        total = temp[start] + temp[end]

        if total < lst[i]:
            start += 1
        elif total > lst[i]:
            end -= 1
        elif total == lst[i]:
            answer += 1
            break
print(answer)
