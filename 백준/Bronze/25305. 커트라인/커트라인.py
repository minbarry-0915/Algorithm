N, k = map(int, input().split())
scores = list(map(int, input().split()))

scores.sort(reverse=True)

cut_line = 0
for i in range(N):
    if i == k - 1:
        cut_line = scores[i]
        break

print(cut_line)
