g = int(input())
x, y = 2, 1 # x: 현재 몸무게 y: 과거 몸무게
result = []

while x <= 100000:
    diff = x * x - y * y
    if diff == g:
        result.append(x)
        x += 1
    elif diff < g:
        x += 1
    else:
        y += 1

if result:
    print('\n'.join(map(str, result)))
else:
    print(-1)