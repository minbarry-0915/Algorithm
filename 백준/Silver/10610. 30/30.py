s = input().strip()

if '0' not in s:
    print(-1)
else:
    total_sum = sum(map(int, s))
    if total_sum % 3 != 0:
        print(-1)
    else:
        print(''.join(sorted(s, reverse=True)))