for _ in range(10):
    t = int(input())
    token = list(input().strip())
    sentence = list(input().strip())
    len_token = len(token)
    len_sentence = len(sentence)
    count = 0
    for i in range(0, len_sentence - len_token + 1):
        window = sentence[i: i + len_token]
        if token[::] == window[::]:
            count += 1
    print(f'#{t} {count}')

