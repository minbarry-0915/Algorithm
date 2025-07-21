import sys
# sys.stdin = open('input.txt','r', encoding='utf-8')
input = sys.stdin.readline

from collections import deque
grid = [list(input()) for _ in range(5)]
idx = [(i,j) for i in range(5) for j in range(5)]
route = [] # 글자 저장용
idx_route = [] # 인덱스 저장용
answer = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def is_valid(r):
    r_copy = deque([i for i in r])

    queue = deque()
    queue.append(r_copy[0])
    r_copy.popleft()
    while queue:
        x,y = queue.popleft()
        for d in range(4):
            nx,ny = x + dx[d], y + dy[d]
            if (nx,ny) in r_copy:
                queue.append((nx,ny))
                r_copy.remove((nx,ny))
    
    # 남아있는 경로는 동떨어져있는 경로임
    if len(r_copy) == 0:
        return True
    return False

def dfs(depth):
    global answer
    if len(route) == 7:
        if route.count('S') >= 4 and is_valid(idx_route):
            answer += 1
        return
    for i in range(depth, 25):
        x,y = idx[i]
        idx_route.append((x,y))
        route.append(grid[x][y])
        dfs(i + 1)
        idx_route.pop()
        route.pop()

dfs(0)
print(answer)
