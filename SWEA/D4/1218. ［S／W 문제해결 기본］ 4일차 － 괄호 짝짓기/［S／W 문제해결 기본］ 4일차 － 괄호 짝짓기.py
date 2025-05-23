for t in range(1, 11):
    n = int(input())
    brackets = list(input().strip())
    stack = []
    pair = {')': '(', ']': '[', '}': '{', '>': '<'}
    valid = 1
    for token in brackets:
        if token in "([{<":
            stack.append(token)
        elif token in ")]}>":
            if not stack or stack[-1] != pair[token]:
                valid = 0
                break
            stack.pop()
    if stack:
        valid = 0
    print(f'#{t} {valid}')