import sys

# sys.stdin = open('input.txt', 'r')

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break

    building = []
    start = end = None

    for z in range(l):
        floor = []
        while True:
            line = input().strip()
            if line == '':
                continue  # 빈 줄은 무시
            floor.append(list(line))
            if len(floor) == r:
                break
        building.append(floor)

    for z in range(l):
        for i in range(r):
            for j in range(c):
                if building[z][i][j] == 'S':
                    start = (z, i, j)
                elif building[z][i][j] == 'E':
                    end = (z, i, j)
    from collections import deque
    def bfs(start):
        visited = [[[-1] * c for _ in range(r)] for _ in range(l)]
        q = deque()
        q.append(start)
        visited[start[0]][start[1]][start[2]] = 0

        while q:
            z,x,y = q.popleft()

            if (z,x,y) == end:
                return visited[z][x][y]

            for d in range(6):
                nz = z + dz[d]
                ny = y + dy[d]
                nx = x + dx[d]

                if 0 <= nz < l and 0 <= nx < r and 0 <= ny < c:
                    if visited[nz][nx][ny] == -1 and building[nz][nx][ny] != '#':
                        visited[nz][nx][ny] = visited[z][x][y] + 1
                        q.append((nz,nx,ny))
        return - 1

    result = bfs(start)
    if result == -1:
        print("Trapped!")
    else:
        print(f"Escaped in {result} minute(s).")
        
    # 케이스 간 공백처리
    temp = input().strip()
    if temp == '':
        continue