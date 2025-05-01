for t in range(1,11):
    code_n = int(input())
    code = list(map(int, input().split()))
    command_n = int(input())
    temp = input().split()

    i = 0
    while i < len(temp):
        command = temp[i]
        x = int(temp[i + 1])
        y = int(temp[i + 2])

        if command == 'I':
            num_lst = list(map(int, temp[i + 3: i + 3 + y]))
            code[x:x] = num_lst
            i += 3 + y
        elif command == 'D':
            del code[x: x + y]
            i += 3
    print(f'#{t}', *code[:10])