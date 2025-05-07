T = int(input())
num_dict = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}
for t in range(1, T + 1):
    n, m = map(int,input().split())
    grid = [input() for _ in range(n)]
    
    # 전략
    # 모든 비트 코드의 마지막이 1로 끝나므로
    # 뒤에서 부터 탐색해서 바코드 추출
    # 시작지점 0 이면 중단
    # 바코드 검사
    found = False
    si,sj = 0,0
    for i in range(n):
        for j in range(m - 1, -1, -1):
            temp = grid[i][j]
            if grid[i][j] == '1': # 시작지점 발견
                sj = j
                si = i
                found = True
                break
        if found:
            break

    # 7개씩 쪼개서 가져오기
    barcode = []
    while grid[si][sj] != '0':
        if sj < 0 or sj >= m: #범위 제한
            break
        temp = grid[si][sj:sj - 7: -1]
        barcode.append(temp[::-1])
        sj -= 7
    # 바코드 숫자 변환
    barcode_to_decimal = []
    for token in barcode[::-1]:
        barcode_to_decimal.append(num_dict[token])
    # 유효성 검사
    total = 0
    for i in range(len(barcode_to_decimal)):
        if i % 2 == 0:
            total += barcode_to_decimal[i] * 3
        else:
            total += barcode_to_decimal[i]
    print(f'#{t} {sum(barcode_to_decimal) if total % 10 == 0 else 0}')