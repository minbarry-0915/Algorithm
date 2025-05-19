# import sys

# sys.stdin = open('input.txt', 'r', encoding='UTF-8')

n = int(input())
nums = list(map(int, input().split()))
answer = [0] * n
stack = []

for i in range(n):
    while stack and nums[stack[-1]] < nums[i]:
        stack.pop()
    if stack:
        answer[i] = stack[-1] + 1
    stack.append(i)

print(* answer)
