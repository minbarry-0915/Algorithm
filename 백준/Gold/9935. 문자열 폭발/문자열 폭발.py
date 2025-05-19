# import sys

#sys.stdin = open('input.txt', 'r', encoding='UTF-8')

text = input().strip()
bomb = input().strip()
stack = []
bomb_len = len(bomb)

for char in text:
    stack.append(char)

    if ''.join(stack[-bomb_len:]) == bomb:
        del stack[-bomb_len:]


if not stack:
    print('FRULA')
else:
    print(''.join(stack))