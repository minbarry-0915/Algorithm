def is_palindrome(target):
    return target[::] == target[::-1]

for _ in range(10):
    t = int(input())
    grid = [input().strip() for _ in range(100)]

    length = 1
    max_len = -1
    while length != 100:
        for i in range(100):
            for j in range(0, 100 - length + 1):
                target = grid[i][j:j + length]
                if is_palindrome(target):
                    max_len = max(max_len, len(target))

        for j in range(100):
            for i in range(0, 100 - length + 1):
                target = ''.join([grid[k][j] for k in range(i, i + length)])
                if is_palindrome(target):
                    max_len = max(max_len, len(target))
        length += 1

    print(f'#{t} {max_len}')