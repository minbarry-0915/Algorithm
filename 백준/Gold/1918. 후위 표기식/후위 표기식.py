#import sys
#sys.stdin = open('input.txt', 'r', encoding='UTF-8')

def postfix(equation):
    stack = []
    result = []

    precedences = {'+': 1, '-': 1, '*': 2, '/': 2}

    for token in equation:
        if token.isalpha():
            result.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedences.get(stack[-1],0) >= precedences[token]:
                result.append(stack.pop())
            stack.append(token)
    while stack:
        result.append(stack.pop())
    return ''.join(result)


equation = list(input())
print(postfix(equation))
