real = [1,1,2,2,2,8]
array = list(map(int, input().split()))

result = [real[i] - array[i] for i in range(len(real))]
print(' '.join(map(str, result)))