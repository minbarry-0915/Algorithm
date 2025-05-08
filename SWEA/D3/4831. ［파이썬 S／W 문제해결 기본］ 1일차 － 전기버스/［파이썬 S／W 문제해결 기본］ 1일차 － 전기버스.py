T = int(input())
for t in range(1, T + 1):
    k,n,m = map(int,input().split())
    stations = list(map(int,input().split()))

    current = 0
    count = 0

    while current + k < n:
        for step in range(k, 0, -1):
            if (current + step) in stations:
                current += step
                count += 1
                break
        else:
            count = 0
            break

    print(f'#{t} {count}')