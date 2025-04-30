def simulate(i,grid):
    dist = 1
    x = 0
    y = i
    while x != 99:
        if y > 0 and grid[x][y - 1] == 1:
            while y > 0 and grid[x][y - 1] == 1:
                y -= 1
                dist += 1
        elif y < n - 1 and grid[x][y + 1] == 1:
            while y < n - 1 and grid[x][y + 1] == 1:
                y += 1
                dist += 1
        x += 1
        dist += 1
    return dist

n = 100
for _ in range(10):
    t = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    answer = 0
    min_dist = int(1e9)
    for i in range(100):
        if grid[0][i] == 1:
            dist = simulate(i,grid)
            if min_dist >= dist:
                min_dist = dist
                answer = i
    print(f'#{t} {answer}')