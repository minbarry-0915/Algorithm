while True:
    lst = sorted(list(map(int, input().split())))
    if lst[0] == lst[1] == lst[2] == 0:
        break
    else:
        res = lst[0] ** 2 + lst[1] ** 2
        if lst[2] ** 2 == res:
            print('right')
        else:
            print('wrong')