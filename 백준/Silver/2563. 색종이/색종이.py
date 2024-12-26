N = int(input())
paper = [[0] * 100 for _ in range(100)]

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            paper[i][j] = 1

black_area = sum(sum(row) for row in paper)
print(black_area)