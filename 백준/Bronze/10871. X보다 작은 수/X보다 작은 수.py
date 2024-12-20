N, X = map(int, input().split())

A = list(map(int,input().rstrip().split()))
result = []
for number in A:
    if number < X:
        result.append(number)
        
print(' '.join(map(str,result)))