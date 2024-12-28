def is_prime(number):
    i = 2
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

if __name__ == '__main__':
    M = int(input())
    N = int(input())
    primes = [i for i in range(M, N + 1) if is_prime(i)]
    if len(primes) == 0:
        print('-1')
    else:
        print(sum(primes))
        print(min(primes))