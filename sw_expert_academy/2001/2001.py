import sys
sys.stdin = open('input.txt','r')

# 테스트 케이스 수 입력
T = int(input())

for test_case in range(1, T + 1):
    # N: 배열 크기, M: 파리채 크기 입력
    N, M = map(int, input().split())
    
    # N x N 배열 입력,                                              
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    max_flies = 0  # 최대로 죽일 수 있는 파리 개수
    
    # 파리채로 죽일 수 있는 파리 수 계산
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            # M x M 파리채 영역 내의 파리 수 합산
            flies = 0
            for x in range(M):
                for y in range(M):
                    flies += grid[i + x][j + y]
            # 최대 파리 수 갱신
            max_flies = max(max_flies, flies)
    
    # 출력 형식에 맞게 결과 출력
    print(f"#{test_case} {max_flies}")
'''
출처 : https://swexpertacademy.com/
'''