
n = int(input())
info = list(map(int,input().split()))

result = [0] * n

for i in range(n):
  taller = info[i]
  for j in range(n):
    if result[j] == 0:
      if taller == 0:
        result[j] = i + 1 
        break
      taller -= 1

print(' '.join(map(str, result)))