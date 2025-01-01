A,B = map(int,input().split())

def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

def lcd(a,b):
    return abs(a * b) // gcd(a,b)

gcd_result = gcd(A,B)
lcd_result = lcd(A,B)

print(gcd_result)
print(lcd_result)
