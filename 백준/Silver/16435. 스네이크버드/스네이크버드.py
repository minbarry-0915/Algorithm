n, l = map(int,input().split())
h = list(map(int,input().split()))
h.sort()

for fruit in h:
    if fruit <= l:
        l += 1
    else:
        break
print(l)