while True:
    x,y = map(int,input().split())
    if x == 0 and y == 0:
        break

    if y != 0 and x % y == 0:
        print('multiple')
    elif x != 0 and y % x == 0:
        print('factor')
    else:
        print('neither')

