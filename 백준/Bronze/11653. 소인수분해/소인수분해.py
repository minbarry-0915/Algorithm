
def prime_factorization(n):
    factors = []
    factor = 2
    while factor * factor <= n:
        while n % factor == 0:
            factors.append(factor)
            n //= factor
        factor += 1

    if n > 1:
        factors.append(n)
    return factors

def main():
    n = int(input())
    if n > 1:
        factors = prime_factorization(n)
        for factor in factors:
            print(factor)


if __name__ == '__main__':
    main()
