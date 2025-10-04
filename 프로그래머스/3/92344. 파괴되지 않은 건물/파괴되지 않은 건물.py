'''
def solution(board, skill):
    n = len(board)
    m = len(board[0])
    for s in skill:
        type, r1,c1,r2,c2,degree = s
        if type == 1: # attack
            for i in range(r1,r2 + 1):
                for j in range(c1, c2 + 1):
                    board[i][j] -= degree
        elif type == 2: # heal
            for i in range(r1,r2 + 1):
                for j in range(c1, c2 + 1):
                    board[i][j] += degree
    return sum(1 for j in range(m) for i in range(n) if board[i][j] >= 1)
'''


def solution(board, skill):
    n, m = len(board), len(board[0])
    # 누적합 배열 초기화
    acc = [[0]*(m+1) for _ in range(n+1)]
    
    for t, r1, c1, r2, c2, degree in skill:
        if t == 1:  # attack
            degree = -degree
        # 4 꼭짓점에만 반영
        acc[r1][c1] += degree
        acc[r1][c2+1] -= degree
        acc[r2+1][c1] -= degree
        acc[r2+1][c2+1] += degree
    
    # 행 누적합
    for i in range(n):
        for j in range(1, m):
            acc[i][j] += acc[i][j-1]
    
    # 열 누적합
    for j in range(m):
        for i in range(1, n):
            acc[i][j] += acc[i-1][j]
    
    # 최종 board 계산
    answer = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] + acc[i][j] > 0:
                answer += 1
                
    return answer