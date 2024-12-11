import sys
sys.stdin = open('input.txt', 'r')

def rotate_90(matrix):
    N = len(matrix)
    arr = []
    for i in range(N):
        new_row = []
        for j in range(N):
            new_row.append(matrix[N - j - 1][i])
        arr.append(new_row)
    return arr

def rotate_180(matrix):
    arr = []
    for row in matrix[::-1]:
        arr.append(row[::-1])
    return arr

def rotate_270(matrix):
    N = len(matrix)
    arr = []
    for i in range(N):
        new_row = []
        for j in range(N):
            new_row.append(matrix[j][N-i-1])
        arr.append(new_row)
    return arr

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    matrix = [list(map(int, input().strip().split())) for _ in range(N)]
    
    rotated_90 = rotate_90(matrix)
    rotated_180 = rotate_180(matrix)
    rotated_270 = rotate_270(matrix)

    # 결과 출력
    print(f'#{test_case}')
    for i in range(N):
        print(''.join(map(str, rotated_90[i])), end=' ')
        print(''.join(map(str, rotated_180[i])), end=' ')
        print(''.join(map(str, rotated_270[i])))


'''
출처 : https://swexpertacademy.com/
'''