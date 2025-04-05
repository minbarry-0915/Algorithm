import sys
input = sys.stdin.readline


n,m = map(int, input().split())
r,c,d = map(int, input().split()) #d 0북, 1동 2남 3서
room = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

cleaned = 0

while True:

    if room[r][c] == 0:
        room[r][c] = 2
        cleaned += 1

    found = False

    for _ in range(4):
        d = (d + 3) % 4
        nx, ny = r + dx[d], c + dy[d]

        if 0 <= nx < n and 0 <= ny < m and room[nx][ny] == 0:
            r, c = nx, ny
            found = True
            break

    if not found:
        back_d = (d + 2) % 4
        bx, by = r + dx[back_d], c + dy[back_d]
        
        if 0 <= bx < n and 0 <= by < m and room[bx][by] != 1:
            r, c = bx, by
        else:
            break
print(cleaned)