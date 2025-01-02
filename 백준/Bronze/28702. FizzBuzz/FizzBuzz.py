def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

n = 0
for i in range(3, 0, -1):
    x = input()
    if x not in ['Fizz', 'Buzz', 'FizzBuzz']:
        # 숫자임: 거리를 계산
        n = int(x) + i
        break
print(fizzbuzz(n))