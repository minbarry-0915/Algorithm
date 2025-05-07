for t in range(1,11):
    n, num_lst = input().split()
    n = int(n)
    stack = []
    for num in num_lst:
        if len(stack) == 0:
            stack.append(num)
        else:
            if stack[-1] == num:
                stack.pop()
            else:
                stack.append(num)
    print(f'#{t}',' ',*stack, sep='')