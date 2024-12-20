N = int(input())
count = N // 4
array = []
for i in range(count):
    array.append('long')

array.append('int')

print(' '.join(array))