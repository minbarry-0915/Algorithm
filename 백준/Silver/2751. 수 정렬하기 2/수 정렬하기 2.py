import sys
numbers = set()

N = int(sys.stdin.readline())
for _ in range(N):
    numbers.add(int(sys.stdin.readline()))

numbers_list = sorted(numbers)
for number in numbers_list:
    print(number)
