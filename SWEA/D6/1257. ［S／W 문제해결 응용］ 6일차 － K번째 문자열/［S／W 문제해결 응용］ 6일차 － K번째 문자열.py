T = int(input())
for t in range(1, T + 1):
    idx = int(input())
    s = input().strip()
    n = len(s)
    substrings_set = set()
    for i in range(n):
        for j in range(i + 1, n + 1):
            window = s[i: j]
            substrings_set.add(s[i: j])

    substrings = list(substrings_set)
    substrings.sort()
    if len(substrings) < idx:
        print('none')
    else:
        print(f'#{t}', end=' ')
        print(''.join(substrings[idx - 1]))