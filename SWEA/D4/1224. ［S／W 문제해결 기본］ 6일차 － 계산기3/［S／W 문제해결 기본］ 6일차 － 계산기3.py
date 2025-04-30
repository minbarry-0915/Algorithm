def get_postfix(formula):
    stack = []
    result = []
    precedence = {'+': 1, '*': 2}
    for token in formula:
        if token.isdigit():
            result.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence[stack[-1]] >= precedence[token]:
                result.append(stack.pop())
            stack.append(token)

    while stack:
        result.append(stack.pop())

    return ''.join(result)


def calculate(postfix):
    stack = []
    for token in postfix:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '*':
                stack.append(a * b)
    return stack[0]


for t in range(1, 11):
    n = int(input())
    formula = input().strip()
    postfix = get_postfix(formula)
    result = calculate(postfix)
    print(f'#{t} {result}')