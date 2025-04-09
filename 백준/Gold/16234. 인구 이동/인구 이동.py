import sys
sys.setrecursionlimit(10 ** 6)
#sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n, l, r = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(n)]

# 동남서북 (시계 방향)
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def dfs(y, x, visited, union):
    for d in range(4):
        ny, nx = y + dy[d], x + dx[d]
        if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
            difference = abs(countries[ny][nx] - countries[y][x])  # 차이
            if l <= difference <= r:  # 범위 이내에 있으면
                visited[ny][nx] = True  # 방문처리
                union.append((ny, nx))  # 연합에 저장
                dfs(ny, nx, visited, union)
    return


days = 0
while True:
    is_moved = False
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                union = [(i, j)] # 연합 초기화
                visited[i][j] = True # 현재 위치 방문처리
                dfs(i, j, visited, union) # dfs 시작
                if len(union) > 1:  # 연합이 하나 이상
                    avg = sum(countries[y][x] for y, x in union) // len(union)  # 평균 계산
                    for y, x in union:
                        countries[y][x] = avg  # 인구 이동 완료
                    is_moved = True # 인구이동 했음
    if not is_moved:  # 움직이지 않으면
        break

    days += 1 # 인구 이동이 일어난 경우에만 날짜 증가
print(days)
