T = 10
for t in range(1, T + 1):
    n = int(input())
    heights = list(map(int, input().split()))

    ans = 0
    for i in range(2, n - 2):
        current = heights[i]
        max_height= max(heights[i - 2: i] + heights[i + 1: i + 3])
        if current > max_height:
            ans += current - max_height

    print(f'#{t} {ans}')
