pair = {')': '(', ']': '[', '}': '{', '>': '<'}

def is_valid_brackets(brackets):
    stack = []
    for c in brackets:
        if c in '([{<':
            stack.append(c)
        elif c in ')]}>':
            if not stack or stack[-1] != pair[c]:
                return 0
            stack.pop()
    return 1


for t in range(1, 11):
    n = int(input())

    brackets = input().strip()
    print(f'#{t} {is_valid_brackets(brackets)}')