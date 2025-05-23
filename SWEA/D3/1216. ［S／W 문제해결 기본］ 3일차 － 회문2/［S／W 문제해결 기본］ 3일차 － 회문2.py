for _ in range(10):
    t = int(input())
    grid = [list(input().strip()) for _ in range(100)]

    max_len = 0
    # 가로 체크
    for n in range(1,101):
        for i in range(100):
            for j in range(100 - n + 1):
                window = grid[i][j:j + n]
                if window[::] == window[::-1]:
                    max_len = max(max_len, len(window))
        # 세로 체크
        for j in range(100):
            for i in range(100 - n + 1):
                window = [grid[k][j] for k in range(i, i + n)]
                if window[::] == window[:: -1]:
                    max_len = max(max_len, len(window))
    print(f'#{t} {max_len}')