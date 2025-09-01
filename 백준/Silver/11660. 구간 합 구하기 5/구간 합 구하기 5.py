n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
queries = [list(map(int,input().split())) for _ in range(m)]

# 1-based indexing으로 안전하게 만들기
prefix_sum = [[0] * (n + 1) for _ in range(n + 1)]

# 1. 누적합 계산
for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix_sum[i][j] = grid[i-1][j-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]

# 2. 쿼리 결과 계산
for x1, y1, x2, y2 in queries:
    result = prefix_sum[x2][y2] - prefix_sum[x1-1][y2] - prefix_sum[x2][y1-1] + prefix_sum[x1-1][y1-1]
    print(result)  