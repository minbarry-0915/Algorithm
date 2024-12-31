while True:
    sentence = input()

    if sentence == '.':
        break

    stack = []
    balanced = True

    for char in sentence:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')' or char == ']':
            if not stack:
                balanced = False
                break
            top = stack.pop()
            if (top != '(' and char == ')') or (top != '[' and char == ']'):
                balanced = False
                break

    if stack:
        balanced = False

    if balanced:
        print('yes')
    else:
        print('no')