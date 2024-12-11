import sys
sys.stdin = open("input.txt", "r")

def count_fit_position(grid, N, K):
    count = 0
    for row in grid:
        length = 0
        for cell in row:
            if cell == 1: #셀이 흰색 : 들어갈 수 있는데 일 때
                length += 1
            else: #벽 만났는데
                if length == K: #길이 만족
                    count += 1 
                length = 0 # 길이 초기화
        if length == K:
            count += 1
            
    for col in range(N):
        length = 0
        for row in range(N):
            if grid[row][col] == 1:
                length += 1
            else:
                if length == K:
                    count += 1
                length = 0
        if length == K:
            count += 1
            
    return count
                

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N , K = map(int, input().split())
    grid = []
    for i in range(N):
        grid.append(list(map(int, input().split())))

    count = count_fit_position(grid, N, K)
    print(f'#{test_case} {count}')
    # ///////////////////////////////////////////////////////////////////////////////////
'''
출처 : https://swexpertacademy.com/
'''