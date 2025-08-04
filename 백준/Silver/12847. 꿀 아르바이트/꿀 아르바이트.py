n,m = map(int,input().split())
t = list(map(int,input().split()))

start = 0
end = 0
max_pay = -1

prefix = [0]
for i in range(n):
    prefix.append(prefix[i] + t[i])

while True:
    if end == n:
        break
    if end - start <= m:
        total = prefix[end] - prefix[start]
        max_pay = max(max_pay, total)
        end += 1 
    else:
        start += 1
print(max_pay)