n = int(input())
a, b, c = map(int, input().split())

dp_max = [a, b, c]
dp_min = [a, b, c]

for _ in range(n - 1):
    a, b, c = map(int, input().split())

    new_max = [0, 0, 0]
    new_min = [0, 0, 0]

    # 0번이 갈수 있는 곳 : 0,1
    new_max[0] = max(dp_max[0], dp_max[1]) + a
    # 1번이 갈수 있는 곳: 0,1,2
    new_max[1] = max(dp_max) + b
    # 2번이 갈수 있는 곳: 1,2
    new_max[2] = max(dp_max[1], dp_max[2]) + c

    # 0번이 갈수 있는 곳 : 0,1
    new_min[0] = min(dp_min[0], dp_min[1]) + a
    # 1번이 갈수 있는 곳: 0,1,2
    new_min[1] = min(dp_min) + b
    # 2번이 갈수 있는 곳: 1,2
    new_min[2] = min(dp_min[1], dp_min[2]) + c
    
    # 갱신
    dp_max = new_max
    dp_min = new_min

print(max(dp_max), min(dp_min))