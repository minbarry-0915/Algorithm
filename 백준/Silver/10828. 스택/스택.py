

import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input().strip())

def push(X,arr):
    arr.append(X)

def pop(arr):
    if arr:
        return arr.pop(-1)
    else:
        return -1

def size(arr):
    return len(arr)

def empty(arr):
    if len(arr) == 0:
        return 1
    else:
        return 0

def top(arr):
    if arr:
        return arr[-1]
    else:
        return -1

stack = []

for _ in range(N):
    command = input().strip().split()
    if command[0] == 'push':
        push(int(command[1]), stack)
    elif command[0] == 'pop':
        print(str(pop(stack)) + '\n')
    elif command[0] == 'size':
        print(str(size(stack)) + '\n')
    elif command[0] == 'empty':
        print(str(empty(stack)) + '\n')
    elif command[0] == 'top':
        print(str(top(stack)) + '\n')
