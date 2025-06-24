import sys

input = sys.stdin.readline

n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]
color_count = [0,0]
'''
접근
전체 배열 검사 다 1이거나 0이면 파란색인지 하얀색인지 리턴
아니면 4분면으로 나눔
재귀(분할정복)
'''

def count_colors(x,y,size):
    if is_same_color(x,y,size): # 해당 섹터가 다 같은 컬러이면
        color = grid[x][y]
        color_count[color] += 1
        return

    # 아니면 4 분할 재귀 실행
    new_size = size // 2
    count_colors(x,y,new_size)
    count_colors(x, y+ new_size, new_size)
    count_colors(x + new_size, y, new_size)
    count_colors(x + new_size, y + new_size, new_size)

def is_same_color(x,y,size):
    base = grid[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if grid[i][j] != base:
                return False
    return True

count_colors(0,0,n)
print(color_count[0])
print(color_count[1])