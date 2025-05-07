for t in range(1,11):
    n = int(input())
    valid = 1
    for _ in range(n):
        parts = input().split()
        idx = int(parts[0])
        value = parts[1]

        if value.isdigit():
            if len(parts) != 2:
                valid = 0
        else:
            if len(parts) != 4:
                valid = 0
    print(f'#{t} {valid}')