K = int(input())

total = 0
stack = []
for i in range(K):
    number = int(input())
    if number != 0:
        stack.append(number)
    else:
        stack.pop()

total = sum(stack)
print(total)