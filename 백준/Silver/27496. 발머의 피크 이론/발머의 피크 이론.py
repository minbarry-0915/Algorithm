
n, l = map(int,input().split())
a = list(map(int,input().split())) 

current = 0
cnt = 0

for i in range(n):
    current += a[i]
    if i >= l:
        current -= a[i - l]
    if 129 <= current <= 138:
        cnt += 1
        
print(cnt)