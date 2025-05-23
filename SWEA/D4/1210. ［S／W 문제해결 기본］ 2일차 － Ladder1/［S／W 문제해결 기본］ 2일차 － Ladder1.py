for _ in range(10):
    t = int(input())
    n = 100
    grid = [list(map(int, input().split())) for _ in range(n)]

    x = 99
    y = grid[99].index(2)

    while x > 0:
        if y > 0 and grid[x][y - 1] == 1:
            while y > 0 and grid[x][y - 1] == 1:
                y -= 1
            x -= 1
        elif y < n - 1 and grid[x][y + 1] == 1:
            while y < n - 1 and grid[x][y + 1] == 1:
                y += 1
            x -= 1
        else:
            x -= 1
    print(f'#{t} {y}')