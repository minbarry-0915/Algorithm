a,b,c = map(int,input().split())

if not(a + b > c):
    c = a + b - 1
elif not(b + c > a):
    a = b + c - 1
elif not(a + c > b):
    b = a + c - 1

print(a+b+c)