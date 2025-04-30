for _ in range(10):
    t = int(input())
    token = input().strip()
    target = input().strip()

    n = len(token)
    answer = 0
    for i in range(0, len(target) - n + 1):
        window = target[i: i + n]
        if window[::] == token[::]:
            answer += 1
    print(f'#{t} {answer}')