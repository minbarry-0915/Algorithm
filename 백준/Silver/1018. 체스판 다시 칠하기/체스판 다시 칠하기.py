# 입력 받기
N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

# 체스판 패턴 정의
chess1 = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
]

chess2 = [
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
]

# 최소 개수를 계산하는 함수
def count_repaints(x, y):
    count1, count2 = 0, 0
    for i in range(8):
        for j in range(8):
            if board[x + i][y + j] != chess1[i][j]:
                count1 += 1
            if board[x + i][y + j] != chess2[i][j]:
                count2 += 1
    return min(count1, count2)

# 슬라이딩 윈도우로 최소값 탐색
min_repaints = float('inf')
for i in range(N - 7):
    for j in range(M - 7):
        min_repaints = min(min_repaints, count_repaints(i, j))

# 결과 출력
print(min_repaints)
