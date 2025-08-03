n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]

prev_max = grid[0][:]
prev_min = grid[0][:]

for i in range(1, n):
    a, b, c = grid[i]

    curr_max = [
        max(prev_max[0], prev_max[1]) + a,
        max(prev_max[0], prev_max[1], prev_max[2]) + b,
        max(prev_max[1], prev_max[2]) + c
    ]
    curr_min = [
        min(prev_min[0], prev_min[1]) + a,
        min(prev_min[0], prev_min[1], prev_min[2]) + b,
        min(prev_min[1], prev_min[2]) + c
    ]

    prev_max = curr_max
    prev_min = curr_min

print(max(prev_max), min(prev_min))