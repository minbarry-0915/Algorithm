for t in range(1, 11):
    n = int(input())
    grid = [list(input().strip()) for _ in range(8)]
    count = 0

    # 가로 체크
    for i in range(8):
        for j in range(8 - n + 1):
            window = grid[i][j:j + n]
            if window[::] == window[::-1]:
                count += 1
    # 세로 체크
    for j in range(8):
        for i in range(8 - n + 1):
            window = [grid[k][j] for k in range(i, i + n)]
            if window[::] == window[:: -1]:
                count += 1
    print(f'#{t} {count}')