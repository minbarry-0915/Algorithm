A, B = map(int, input().split())

count = 1
while B > A:
    if B % 10 == 1:
        B //= 10
    elif B % 2 == 0:
        B //= 2
    else:
        break
    count += 1

if B == A:
    print(count)
else:
    print(-1)