while True:
    sides = list(map(int, input().split()))
    if sides == [0,0,0]:
        break

    sorted_sides = sorted(sides)
    if sorted_sides[2] >= sorted_sides[0] + sorted_sides[1]:
        print('Invalid')
    else:
        if sides[0] == sides[1] and sides[0] == sides[2] and sides[1] == sides[2]:
            print('Equilateral')
        elif sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
            print('Isosceles')
        elif sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]:
            print('Scalene')