n = int(input())
scores = [int(input()) for _ in range(n)]

count = 0
for i in range(n - 2, -1, -1):
    if scores[i] >= scores[i + 1]:
        diff = scores[i] - (scores[i + 1] - 1)
        count += diff
        scores[i] = scores[i + 1] - 1

print(count)
