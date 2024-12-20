N = int(input())
numbers = list(map(int,input().rstrip().split()))
keyword = int(input())
count = 0
for number in numbers:
    if keyword == number:
        count += 1
        
print(count)