import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

def push(X, arr):
    arr.append(X)

def pop(arr):
    if arr:
        return arr.pop(0)
    else:
        return -1

def size(arr):
    return len(arr)

def empty(arr):
    if len(arr) == 0:
        return 1
    else:
        return 0

def front(arr):
    if arr:
        return arr[0]
    else:
        return -1

def back(arr):
    if arr:
        return arr[-1]
    else:
        return -1

queue = []
for _ in range(N):
    command = input().split()
    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'pop':
        print(str(pop(queue)) + '\n')
    elif command[0] == 'size':
        print(str(size(queue)) + '\n')
    elif command[0] == 'empty':
        print(str(empty(queue)) + '\n')
    elif command[0] == 'front':
        print(str(front(queue)) + '\n')
    elif command[0] == 'back':
        print(str(back(queue)) + '\n')
