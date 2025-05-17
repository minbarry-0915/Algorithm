import sys

# sys.stdin = open('input.txt', 'r', encoding='UTF-8')

n, b = map(int, input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]

def matrix_mul(A,B):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] %= 1000
    return result

def matrix_pow(A,B):
    if B == 1:
        return [[element % 1000 for element in row] for row in A]
    temp = matrix_pow(A, B // 2)
    if B % 2 == 0:
        return matrix_mul(temp, temp)
    else:
        return matrix_mul(matrix_mul(temp, temp), A)

result = matrix_pow(matrix,b)
for row in result:
    print(* row)


