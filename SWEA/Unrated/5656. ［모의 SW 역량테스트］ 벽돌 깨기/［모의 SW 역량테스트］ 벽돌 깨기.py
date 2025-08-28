from collections import deque

T = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def choose_0_to_w(n, w, depth, cases, case):
    if depth == n:
        cases.append(case[:])
        return
    for i in range(w):
        case.append(i)
        choose_0_to_w(n, w, depth + 1, cases, case)
        case.pop()
    return


for t in range(1, T + 1):
    n, w, h = map(int,input().split())
    grid = [list(map(int,input().split())) for _ in range(h)]

    # 어디에 던질건지에 대한 경우의 수 만들기
    cases = []
    choose_0_to_w(n, w, 0,cases,[])

    min_remaining = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0:
                min_remaining += 1

    def bfs(x,y,grid_copy):
        queue = deque()
        queue.append([x,y])
        visited = [[False] * w for _ in range(h)]
        visited[x][y] = True
        affected = [[x, y]]

        while queue:
            x,y = queue.popleft()
            affecting_range = grid_copy[x][y]
            for a in range(1, affecting_range):
                for d in range(4):
                    nx,ny = x + dx[d] * a, y + dy[d] * a
                    if 0 <= nx < h and 0 <= ny < w and grid_copy[nx][ny] != 0 and not visited[nx][ny]:
                        queue.append([nx,ny])
                        affected.append((nx,ny))
                        visited[nx][ny] = True
        return affected

    def apply_gravity(grid_copy):
        for col in range(w):
            stack = []
            for row in range(h - 1, -1, -1):
                if grid_copy[row][col] != 0:
                    stack.append(grid_copy[row][col])
            # 다시 채워 넣기
            for row in range(h - 1, -1, -1):
                if stack:
                    grid_copy[row][col] = stack.pop(0)
                else:
                    grid_copy[row][col] = 0

    def simulation(case):
        grid_copy = [row[::] for row in grid]

        for y in case:
            # 충돌 행 찾기
            x = 0
            while x < h and grid_copy[x][y] == 0:
                x += 1
            if x == h:  # 해당 열이 전부 비어있으면 continue
                continue

            affected = bfs(x, y, grid_copy)
            for (xx, yy) in affected:
                grid_copy[xx][yy] = 0

            apply_gravity(grid_copy)

        remaining = sum(1 for i in range(h) for j in range(w) if grid_copy[i][j] != 0)
        return remaining

    # 케이스 별로 시물레이션 진행
    for case in cases:
        min_remaining = min(min_remaining, simulation(case))
    print(f'#{t} {min_remaining}')

