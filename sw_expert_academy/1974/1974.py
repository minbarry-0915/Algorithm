
import sys
sys.stdin = open("input.txt", "r")

def has_duplicates(arr):
    return len(arr) != len(set(arr))

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    grid = []
    total_result = 1
    for i in range(9):
        grid.append(list(map(int, input().split())))
    
    for row in range(9):
        if has_duplicates(grid[row]):
            total_result = 0
            break
        
    for col in range(9):
        arr = [grid[row][col] for row in range(9)]
        if has_duplicates(arr):
            total_result = 0
            break
        
    for box_row in range(0,9,3):
        for box_col in range(0,9,3):
            arr = []
            for i in range(3):
                for j in range(3):
                    arr.append(grid[box_row + i][box_col + j])
            if has_duplicates(arr):
                total_result = 0
                break
            
    print(f'#{test_case} {total_result}')
        
    # ///////////////////////////////////////////////////////////////////////////////////
'''
출처 : https://swexpertacademy.com/
'''