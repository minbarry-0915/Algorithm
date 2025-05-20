T = int(input())
for t in range(1, T + 1):
    idx = int(input())
    s = list(input())

    dict = []
    dict.append(s[:])
    for _ in range(len(s) - 1):
        s.pop(0)
        dict.append(s[:])
    dict.sort()
    print(f'#{t}', end=' ')
    if len(dict) < idx or dict[idx] is None:
        print("none")
    else:
        print(''.join(dict[idx - 1]))