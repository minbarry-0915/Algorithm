N = int(input())
ropes = [int(input().strip()) for _ in range(N)]

ropes.sort(reverse = True)

max_weight = 0
for i in range(N):
    max_weight = max(max_weight, ropes[i] * (i + 1))

print(max_weight)