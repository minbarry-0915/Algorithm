n = int(input())
lst = list(map(int, input().split()))
dp_i = [1] * n
dp_d = [1] * n

for i in range(n):
    for j in range(i):
        if lst[i] > lst[j]:
            dp_i[i] = max(dp_i[i], dp_i[j] + 1)

for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if lst[i] > lst[j]:
            dp_d[i] = max(dp_d[i], dp_d[j] + 1)

dp = [dp_i[i] + dp_d[i] - 1  for i in range(n)]
print(max(dp))