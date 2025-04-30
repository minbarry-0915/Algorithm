for t in range(1, 11):
    n = int(input())  # 항상 100
    grid = [list(map(int, input().split())) for _ in range(n)]

    count = 0
    for j in range(100):  # 열 단위
        flag = False  # N극을 만났는지 여부
        for i in range(100):  # 위에서 아래로
            if grid[i][j] == 1:
                flag = True
            elif grid[i][j] == 2:
                if flag:
                    count += 1
                    flag = False  # 다시 초기화

    print(f'#{t} {count}')