for _ in range(10):
    t_num = int(input())
    grid = [list(map(int, input().split())) for _ in range(100)]
    n = 100
    min_y = -1

    for i in range(n):
        if grid[99][i] == 2:
            x, y = 99, i
            break

    while x > 0:
        if y > 0 and grid[x][y - 1] == 1:
            while y > 0 and grid[x][y - 1] == 1:
                y -= 1
        elif y < n - 1 and grid[x][y + 1] == 1:
            while y < n - 1 and grid[x][y + 1] == 1:
                y += 1
        x -= 1

    print(f'#{t_num} {y}')