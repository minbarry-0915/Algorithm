import sys

input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))  # operator
min_val = float('inf')
max_val = float('-inf')


def dfs(depth, total, plus, minus, mul, div):
    global min_val, max_val

    if depth == n:
        min_val = min(total, min_val)
        max_val = max(total, max_val)
        return

    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, mul, div)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, mul, div)
    if mul:
        dfs(depth + 1, total * num[depth], plus, minus, mul - 1, div)
    if div:
        if total < 0:
            dfs(depth + 1, -(-total // num[depth]), plus, minus, mul, div - 1)
        else:
            dfs(depth + 1, total // num[depth], plus, minus, mul, div - 1)

dfs(1, num[0], op[0], op[1],op[2], op[3])
print(max_val)
print(min_val)
