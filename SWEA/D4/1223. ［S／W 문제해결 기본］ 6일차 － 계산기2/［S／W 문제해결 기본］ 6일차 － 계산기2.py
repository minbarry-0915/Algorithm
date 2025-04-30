def infix_to_postfix(formula):
    stack = []
    result = []
    precedence = {'+': 1, '*': 2}

    for token in formula:
        if token.isdigit():
            result.append(token)
        else:
            while stack and precedence[stack[-1]] >= precedence[token]:
                result.append(stack.pop())
            stack.append(token)

    while stack:
        result.append(stack.pop())

    return ''.join(result)


def calculate(formula):
    stack = []

    for token in formula:
        if token.isdigit():
            stack.append(token)
        else:
            b = int(stack.pop())
            a = int(stack.pop())
            if token == '+':
                stack.append(a + b)
            elif token == '*':
                stack.append(a * b)
    return stack[-1]

for t in range(1, 11):
    n = int(input())
    formula = input().strip()
    formula = infix_to_postfix(formula)
    result = calculate(formula)
    print(f'#{t} {result}')