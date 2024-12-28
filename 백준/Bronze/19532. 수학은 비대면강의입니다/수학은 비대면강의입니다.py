
a,b,c,d,e,f = map(int,input().split())

result_x, result_y = 0,0
for x in range(-999,1000):
    for y in range(-999,1000):
        if a * x + b * y == c and d *x + e * y == f:
            result_x = x
            result_y = y

print(result_x, result_y)