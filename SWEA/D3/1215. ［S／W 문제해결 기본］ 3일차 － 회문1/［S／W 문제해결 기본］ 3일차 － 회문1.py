def is_palindrome(target):
    return target[::] == target[::-1]


for t in range(1, 11):
    n = int(input())
    grid = [input().strip() for _ in range(8)]

    count = 0
    # 가로 검사
    for i in range(8):
        for j in range(8 - n + 1):
            target = grid[i][j: j + n]
            if is_palindrome(target):
                count += 1
    # 세로 검사
    for j in range(8):
        for i in range(8 - n + 1):
            target = ''.join([grid[k][j] for k in range(i, i + n)])
            if is_palindrome(target):
                count += 1

    print(f'#{t} {count}')