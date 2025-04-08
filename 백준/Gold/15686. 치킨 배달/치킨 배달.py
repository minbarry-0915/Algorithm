import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
# 동서남북
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
houses = []
chickens = []
# 0 빈칸, 1 집, 2 치킨집
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:  # 집 발견
            houses.append((i, j))
        elif maps[i][j] == 2:  # 치킨집 발견
            chickens.append((i, j))  # 좌표, 선택 받은 집 갯수

answer = int(1e9)
selected = []

def dfs(depth, start):
    global answer
    if depth == m: # 치킨집 선택 끝나면 거리 계산
        city_distance = 0
        for hx, hy in houses:
            min_dist = int(1e9)
            for cx, cy in selected:
                dist = abs(hx - cx) + abs(hy - cy)
                min_dist = min(min_dist, dist)
            city_distance += min_dist
        answer = min(answer, city_distance)
        return

    for i in range(start, len(chickens)):
        selected.append(chickens[i]) #치킨집 하나 고르기
        dfs(depth + 1, i + 1) #다음 치킨집 고르기
        selected.pop() #백트랙킹
        
dfs(0, 0)
print(answer)