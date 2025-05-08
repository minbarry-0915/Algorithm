T = int(input())
for t in range(1, T + 1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    sum_arr = []
    for i in range(0, n - m + 1):
        window = arr[i: i + m]
        sum_arr.append(sum(window))

    print(f'#{t} {max(sum_arr) - min(sum_arr)}')
