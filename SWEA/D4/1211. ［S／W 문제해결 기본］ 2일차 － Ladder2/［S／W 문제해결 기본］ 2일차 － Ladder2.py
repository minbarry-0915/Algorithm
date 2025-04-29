

N = 100
T = 10

for _ in range(T):
    t_num = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]

    min_dist = int(1e9)
    answer = 0

    for start_y in range(N):
        if grid[0][start_y] == 1:
            x, y = 0, start_y
            cnt = 0
            visited = [[False] * N for _ in range(N)]
            while x < N - 1:
                visited[x][y] = True
                # 왼쪽
                if y > 0 and grid[x][y - 1] == 1 and not visited[x][y - 1]:
                    while y > 0 and grid[x][y - 1] == 1:
                        y -= 1
                        cnt += 1
                        visited[x][y] = True
                # 오른쪽
                elif y < N - 1 and grid[x][y + 1] == 1 and not visited[x][y + 1]:
                    while y < N - 1 and grid[x][y + 1] == 1:
                        y += 1
                        cnt += 1
                        visited[x][y] = True
                # 아래로
                x += 1
                cnt += 1
            if cnt < min_dist:
                min_dist = cnt
                answer = start_y

    print(f"#{t_num} {answer}")
