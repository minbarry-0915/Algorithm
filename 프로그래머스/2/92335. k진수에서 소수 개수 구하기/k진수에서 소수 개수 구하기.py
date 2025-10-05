import math

def into_base(n,k):
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if n == 0:
        return '0'
    result = ''
    while n > 0:
        result = digits[n % k] + result 
        n //= k
    return result

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.isqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    k_base = into_base(n,k)
    parts = k_base.split("0")
    count = 0

    for part in parts:
        if part:
            num = int(part)
            if is_prime(num):
                count += 1    
    return count

# 테스트
print(solution(437674, 3))
