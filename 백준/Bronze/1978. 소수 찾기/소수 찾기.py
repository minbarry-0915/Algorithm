N = int(input())
numbers = list(map(int, input().split()))

def get_factors(n):
    factors = []
    i = 1
    while i < n:
        if n % i == 0:
            factors.append(i)
        i += 1
    return factors

def is_prime(n):
    factors = get_factors(n)
    if len(factors) == 1:
        return True
    else:
        return False
    
result = 0
for number in numbers:
    if is_prime(number):
        result += 1

print(result)