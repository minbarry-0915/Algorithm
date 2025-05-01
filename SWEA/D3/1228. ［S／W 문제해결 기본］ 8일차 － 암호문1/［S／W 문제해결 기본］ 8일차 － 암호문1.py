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
        num_lst = (map(int, temp[i + 3: i + 3 + y]))
        for j, num in enumerate(num_lst):
            code.insert(x + j, num)
        i += 3 + y

    print(f'#{t}', *code[:10])