T = int(input())

for test in range(T):
    ps = input().strip()

    balanced = True
    stack = []
    for char in ps:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                balanced = False
                break
            stack.pop()
            

    if stack:
        balanced = False

    if balanced:
        print('YES')
    else:
        print('NO')
