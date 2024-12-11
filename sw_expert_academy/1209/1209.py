
import sys
sys.stdin = open("input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    case_number = int(input()) 
    #2차원 행렬 생성
    #한줄에 100개의 숫자 100개의 줄이므로 
    matrix = [list(map(int, input().split())) for _ in range(100)]
    
    # row_sum = [sum(row) for row in matrix] 
    row_sum = []
    for row in matrix:
        total = sum(row)
        row_sum.append(total)
    
    # col_sum = [sum(matrix[row][col] for row in range(100)) for col in range(100)]
    col_sum = []
    for col in range(100):
        total = 0
        for row in range(100):
            total += matrix[row][col]
        col_sum.append(total)

    diagonal1_sum = sum(matrix[i][i] for i in range(100)) #왼쪽 위-> 오른쪽 아래
    diagonal2_sum = sum(matrix[i][99-i] for i in range(100)) #왼쪽아래 -> 오른쪽 위 
    
    #최댓값 추출
    max_sum = max(max(row_sum), max(col_sum), diagonal1_sum, diagonal2_sum)
    
    #결과 출력
    print(f'#{test_case} {max_sum}')
    
    # ///////////////////////////////////////////////////////////////////////////////////
