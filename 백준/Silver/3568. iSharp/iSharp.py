import sys

# sys.stdin = open('input.txt', 'r', encoding='utf-8')

input = sys.stdin.readline

line = input().strip().rstrip(';')
tokens = line.split()
#print(tokens)

base_type = tokens[0]
variables = ' '.join(tokens[1:]).split(',')
#print(variables)

for var in variables:
    var = var.strip()
    name = '' # 변수명 저장
    tail = '' # 잡다한거 저장

    for i in range(len(var)):
        if var[i].isalpha():
            name += var[i]
        else:
            tail += var[i]

    reversed_tail = ''
    for ch in reversed(tail):
        if ch == ']':
            reversed_tail += '[]'
        elif ch == '[':
            continue
        else:
            reversed_tail += ch

    print(f'{base_type}{reversed_tail} {name};')