
import sys
sys.stdin = open("input.txt", "r")


def is_safe(row, col):
    for prev_row in range(row):
        if queen_positions[prev_row] == col or \
            queen_positions[prev_row] - prev_row == col - row or \
                queen_positions[prev_row] + prev_row == col + row: 
                    return False
    return True

def place_queens(row):
    # 다 돌았으면 경로 하나 찾은거임 솔루션 추가
    if row == N:
        global count
        count += 1
        return
    
    for col in range(N):
        if is_safe(row,col): #맞는 경로이면
            queen_positions[row] = col #저장
            place_queens(row+1) #다음 열 재귀함수로 호출

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    queen_positions = [-1] * N 
    count = 0
    place_queens(0)
    
    print(f'#{test_case} {count}')
    # ///////////////////////////////////////////////////////////////////////////////////
