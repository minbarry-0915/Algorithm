import sys
sys.stdin = open("input.txt", "r")

def max_sum_product(A,B):
    N = len(A)
    M = len(B)
    max_sum = 0
    
    if N > M: #A가 무조건 짧게
        A,B = B, A
        N,M = M, N
    
    for start in range(0, M-N+1):  # A를 B와 겹치게 슬라이딩
        current_sum = 0
        for i in range(N):
            # B의 인덱스가 유효한 경우에만 곱합니다.
            current_sum += A[i] * B[start + i]
        max_sum = max(max_sum, current_sum)
    
    return max_sum

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N,M = map(int, input().strip().split())
    
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    max_sum = max_sum_product(Ai, Bj)
    
    print(f'#{test_case} {max_sum}')
    
    
    # ///////////////////////////////////////////////////////////////////////////////////
'''
https://swexpertacademy.com/
'''