N, K = map(int, input().split())
currencies = [int(input()) for _ in range(N)]

currencies.sort(reverse=True)

count = 0
for coin in currencies:
    if K == 0:
        break
    count += K // coin
    K = K % coin

print(count)