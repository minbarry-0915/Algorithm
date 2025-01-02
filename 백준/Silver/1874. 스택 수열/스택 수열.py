import sys
input = sys.stdin.readline

n = int(input())
stack = []
answer = []
curr = 1
flag = 0
for i in range(n):
    num = int(input())
    while curr <= num:
        stack.append(curr)
        answer.append('+')
        curr += 1

    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        flag = 1
        break

if flag == 0:
    for i in answer:
        print(i)