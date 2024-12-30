N = int(input())
A = set(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

for number in B:
    print(1) if number in A else print(0)