n, l = map(int, input().split())
locs = list(map(int, input().split()))

locs.sort()
count = 0
i = 0

while i < n:
    start = locs[i]

    end = start + l - 1
    count += 1

    while i < n and locs[i] <= end:
        i += 1

print(count)