from collections import Counter
T = int(input())
for t in range(1, T + 1):
    n = int(input())
    arr = input().strip()

    count = Counter(arr)
    max_num = 0
    max_freq = 0
    for num, freq in count.items():
        if freq >= max_freq:
            max_num = max(max_num, int(num))
            max_freq = freq
    print(f'#{t} {max_num} {max_freq}')