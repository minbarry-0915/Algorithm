import sys
sys.stdin = open('input.txt', 'r')


for test_case in range(1,11):
    height = int(input())
    matrix = [list(map(int,input().split())) for _ in range(100)]
    
    total = 0
    # 1이 붉은색(N) 2가 파란색(S)
    # 위가 N 아래가 S, 그러므로 N 만나고 S만나야지 교착 상태, 아니면 패스
    #교착 상태는 두개 다 있을때만 성립
    for col in range(100):
        state = 0 #0 : 정상 , 1: 교착
        for row in range(100):
            if matrix[row][col] == 1:
                state = 1
            if matrix[row][col] == 2 and state == 1:
                total += 1
                state = 0 # 상태 초기화
                
                

    print(f'#{test_case} {total}')