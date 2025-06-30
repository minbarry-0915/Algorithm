'''
접근 1. 유니온 파인드
우리는 만약 두 직사각형이 서로 교차한다면, 두 직사각형을 모두 펜을 떼지 않고 그릴 수 있다는 사실을 알고 있다.
다시 말해, 만약 두 직사각형이 만나지 않는다면 무조건 펜을 한 번은 떼야만 그릴 수 있다는 뜻이다.
여러 직사각형끼리 만나서 붙어있는 거를 하나의 "그룹"이라고 하면, 우리는 한 "그룹"을 펜을 떼지 않고 그릴 수 있다.(PU명령이 필요 없음.)
따라서, PU명령의 최솟값을 구하라는 뜻은, 분리 집합을 이용하여 직사각형 "그룹"의 개수가 몇 개인지 구하라는 뜻과 거의 같다.
'''
# def get_parent(x):
#     if parent[x] == x:
#         return x
#     parent[x] = get_parent(parent[x])
#     return parent[x]
#
# def union_find(x1, x2):
#     x1_parent = get_parent(x1)
#     x2_parent = get_parent(x2)
#     if x1_parent < x2_parent:
#         parent[x2_parent] = x1_parent
#     else:
#         parent[x1_parent] = x2_parent
#
# def intersect_check(i, j):
#     x01, y01, x02, y02 = square[i]
#     x11, y11, x12, y12 = square[j]
#     if (x12 < x01 or x11 > x02
#             or y11 > y02 or y12 < y01
#             or (x01 < x11 < x12 < x02 and y01 < y11 < y12 < y02)
#             or (x11 < x01 < x02 < x12 and y11 < y01 < y02 < y12)):
#         return False
#     return True
#
# n = int(input())
# square = [list(map(int, input().split())) for _ in range(n)]
# parent = [i for i in range(n)]
# start_point = [0, 0]
# for i in range(n):
#     for j in range(i+1, n):
#         if intersect_check(i, j):
#             union_find(i, j)
#
# union_set = set()
# intersect_point = 0
# for i in range(n):
#     x1, y1, x2, y2 = square[i]
#     if (not intersect_point
#             and ((x1 <= start_point[0] <= x2 and start_point[1] in [y1, y2])
#                  or (y1 <= start_point[1] <= y2 and start_point[0] in [x1, x2]))):
#         intersect_point = 1
#     idx = get_parent(i)
#     if idx not in union_set:
#         union_set.add(idx)
# print(len(union_set) - intersect_point)

'''
접근 2. bfs 섬 세기
두배로 스케일링, 인덱스 계산을 위해 양수처리
섬 세고, 1000,1000(가운데)지점 포함시 -1
'''
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(sx,sy):
    q = deque()
    q.append((sx,sy))
    visited[sx][sy] = True
    while q:
        x,y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            
            # 범위내, 미방문, 선분있음
            if 0 <= nx < 2001 and 0 <= ny < 2001 and not visited[nx][ny] and grid[nx][ny] != 0:
                visited[nx][ny] = True
                q.append((nx,ny))

n = int(input())
rects = [list(map(lambda x: int(x) * 2 + 1000,input().split())) for _ in range(n)]
grid =[[0] * 2001 for _ in range(2001)]

# 선 그리기
idx = 1
for x1,y1,x2,y2 in rects:
    for y in range(y1, y2 + 1):
        grid[x1][y] = grid[x2][y] = idx
    for x in range(x1,x2 + 1):
        grid[x][y1] = grid[x][y2] = idx
    idx += 1

visited = [[False] * 2001 for _ in range(2001)]
answer = 0

for x1,y1,x2,y2 in rects:
    if not visited[x1][y1]:
        bfs(x1,y1)
        answer += 1
answer += -1 if grid[1000][1000] != 0 else 0
print(answer)


