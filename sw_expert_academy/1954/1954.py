# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    snail = [[0] * N for _ in range(N)] # N*N 이차원 배열 초기화
    x, y, direction = 0,0,0
    num = 1
    
    for num in range(1, N*N+1):
        snail[x][y] = num
        nx = x + dx[direction]
        ny = y + dy[direction]
        
        if nx < 0 or nx >= N or ny < 0 or ny >= N or snail[nx][ny] != 0:
            direction = (direction + 1) % 4
            nx  = x + dx[direction]
            ny = y + dy[direction]
        
        x,y = nx, ny
    
    print(f'#{test_case}')
    for row in snail:
        print(" ".join(map(str,row)))
    # ///////////////////////////////////////////////////////////////////////////////////
