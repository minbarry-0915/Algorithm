n = int(input())

from collections import deque
queue = deque()
for _ in range(n):
    command = input().split()

    if command[0] == 'push_back':
        num = int(command[1])
        queue.append(num)
    elif command[0] == 'push_front':
        num = int(command[1])
        queue.appendleft(num)
    elif command[0] == 'pop_front':
        if len(queue) != 0:
            print(queue.popleft())
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if len(queue) != 0:
            print(queue.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif command[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[len(queue) - 1])