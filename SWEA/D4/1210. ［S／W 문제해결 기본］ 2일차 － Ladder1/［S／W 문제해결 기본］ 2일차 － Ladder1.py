
for _ in range(1, 11) :
    tc = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]

    result = 0
    for i in range(100) :
        if data[0][i] == 1 : # 시작
            x, y = 0, i
            while x != 99 :
                x += 1
                if y > 0 and data[x][y-1] == 1 :
                    while y > 0 and data[x][y-1] == 1 :
                        y -= 1
                elif y < 99 and data[x][y+1] == 1 :
                    while y < 99 and data[x][y+1] == 1 :
                        y += 1

            if data[x][y] == 2 :
                result = i
                break

    print('#%d %d' % (tc, result))