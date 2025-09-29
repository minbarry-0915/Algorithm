import sys

n = int(input())
cranes = list(map(int,input().split()))
m = int(input())
boxed = list(map(int,input().split()))

cranes.sort(reverse=True)
boxed.sort(reverse=True)

# 가장 큰 크레인으로도 못옮김
if boxed[0] > cranes[0]:
    print(-1)
    sys.exit()

time = 0
moved = [False] * m
count = 0

while count < m:
    idx = 0
    box_idx = 0
    while idx < n and box_idx < m:
        if not moved[box_idx] and cranes[idx] >= boxed[box_idx]:
            moved[box_idx] = True
            count += 1
            idx += 1
        box_idx += 1
    time += 1
print(time)