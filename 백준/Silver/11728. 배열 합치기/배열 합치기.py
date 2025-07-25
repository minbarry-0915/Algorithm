n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

i = j = 0
result = []

while i < n and j < m:
    if a[i] < b[j]:
        result.append(a[i])
        i += 1
    else:
        result.append(b[j])
        j += 1

result.extend(a[i:])
result.extend(b[j:])

print(' '.join(map(str, result)))