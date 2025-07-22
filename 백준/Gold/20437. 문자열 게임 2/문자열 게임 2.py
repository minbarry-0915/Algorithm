from collections import defaultdict

T = int(input())

for _ in range(T):
    w = input().strip()
    k = int(input())

    pos_dict = defaultdict(list)

    for idx,char in enumerate(w):
        pos_dict[char].append(idx)

    min_len = int(1e9)
    max_len = -1

    for char in pos_dict:
        indices = pos_dict[char]
        if len(indices) < k:
            continue

        for i in  range(len(indices) - k + 1):
            start = indices[i]
            end = indices[i + k - 1]
            length = end - start + 1

            min_len = min(min_len, length)
            max_len = max(max_len, length)

    if min_len == int(1e9):
        print(-1)
    else:
        print(min_len, max_len)