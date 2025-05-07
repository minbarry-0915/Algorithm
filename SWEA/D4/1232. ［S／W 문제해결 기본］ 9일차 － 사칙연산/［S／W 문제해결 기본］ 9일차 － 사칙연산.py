def evaluate(now):
    val = tree[now]
    if val[0].isdigit():  # 숫자인 경우
        return int(val[0])

    left = evaluate(val[1])
    right = evaluate(val[2])
    op = val[0]

    if op == '+':
        return left + right
    elif op == '-':
        return left - right
    elif op == '*':
        return left * right
    elif op == '/':
        return left // right

for t in range(1, 11):
    n = int(input())
    tree = [None] * (n + 1)
    for _ in range(n):
        parts = input().split()
        idx = int(parts[0])
        if len(parts) == 2:  # 숫자 노드
            tree[idx] = (parts[1],)
        else:  # 연산자 노드
            op = parts[1]
            left = int(parts[2])
            right = int(parts[3])
            tree[idx] = (op, left, right)

    result = evaluate(1)
    print(f'#{t} {result}')