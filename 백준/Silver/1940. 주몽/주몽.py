n = int(input())
m = int(input())
numbers = list(map(int,input().split()))
numbers.sort()

start = 0
end = n - 1
answer = 0
while start < end:
    total = numbers[start] + numbers[end]
    
    if total == m:
        answer += 1

    if total < m:
        start += 1
    else:
        end -= 1
print(answer)