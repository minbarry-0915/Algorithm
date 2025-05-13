import sys
# sys.stdin = open('input.txt', 'r', encoding='utf-8')

board = input().strip()

polynomio = ['AAAA', 'BB']

board_splited = board.split('.')
result = []
for seg in board_splited:
    n = len(seg)
    if n % 2 != 0: #2나 4로 안나눠지면 안되는거임
        print(-1)
        exit()
    result.append('AAAA' * (n // 4) + 'BB' * ((n % 4) // 2))
print('.'.join(result))