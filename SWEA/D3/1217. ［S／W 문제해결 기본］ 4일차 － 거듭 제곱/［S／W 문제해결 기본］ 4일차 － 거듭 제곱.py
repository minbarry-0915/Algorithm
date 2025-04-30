def exponential(n,m):
    if m == 0:
        return 1
    return n * exponential(n, m - 1)

for _ in range(10):
    t = int(input())
    n,m = map(int, input().split())

    answer = exponential(n,m)
    print(f'#{t} {answer}')