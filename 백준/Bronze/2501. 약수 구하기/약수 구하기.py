N, K = map(int, input().split())

i = 1
factor = []
while i <= N:
    if N % i == 0:
       factor.append(i)
    i += 1
if len(factor) < K:
    print(0)
else:
    print(factor[K - 1])