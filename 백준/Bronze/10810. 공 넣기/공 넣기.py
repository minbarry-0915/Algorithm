N, M = map(int, input().split())

buckets = [0 for _ in range(N)]
for _ in range(M):
    i, j, k = map(int, input().rstrip().split())
    for index in range(i - 1, j):
        buckets[index] = k

print(' '.join(map(str, buckets)))