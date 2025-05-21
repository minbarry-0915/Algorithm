T = int(input())
for t in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    sticks = dict()
    starts = set()
    ends = set()

    for i in range(0, n * 2, 2):
        s, e = arr[i], arr[i + 1]
        sticks[s] = e
        starts.add(s)
        ends.add(e)

    start_point = (starts - ends).pop()

    result = []
    c = start_point
    while c in sticks:
        result.append(c)
        result.append(sticks[c])
        c = sticks[c]

    print(f'#{t}', * result)
