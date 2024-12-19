def getQuadrant(x,y):
    if x > 0 and y > 0:
        print(1)
    elif x > 0 and y < 0:
        print(4)
    elif x < 0 and y > 0:
        print(2)
    elif x < 0 and y < 0:
        print(3)

x = int(input())
y = int(input())
getQuadrant(x,y)