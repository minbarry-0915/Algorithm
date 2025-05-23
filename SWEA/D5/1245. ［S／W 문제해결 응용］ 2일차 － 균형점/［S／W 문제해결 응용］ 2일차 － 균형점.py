T = int(input())
for t in range(1, T + 1):
    n = int(input())
    temp = list(map(int, input().split()))
    locs = temp[:n]
    mass = temp[n:]
    results = []

    for i in range(n - 1):
        left = locs[i]
        right = locs[i + 1]

        while right - left > 1e-12:
            mid = (left + right) / 2
            left_f = 0
            right_f = 0

            for j in range(n):
                if locs[j] < mid:
                    left_f += mass[j] / ((mid - locs[j]) ** 2)
                else:
                    right_f += mass[j] / ((locs[j] - mid) ** 2)

            if left_f > right_f:
                left = mid
            else:
                right = mid
        results.append(mid)

    print(f'#{t}', end=' ')
    for r in results:
        print(f'{r:.10f}', end=' ')
    print()