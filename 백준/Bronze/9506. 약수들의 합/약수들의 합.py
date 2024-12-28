def get_factor(n: int):
    i = 1
    factor = []
    while i < n:
        if n % i == 0:
            factor.append(i)
        i += 1
    return factor

def is_perfect_number(n: int):
    factor = get_factor(n)
    sum_factor = sum(factor)
    if sum_factor == n:
        return factor
    else:
        return []

while True:
    n = int(input())
    if n == -1:
        break
    result = is_perfect_number(n)
    if not result:
        print(f'{n} is NOT perfect.')
    else:
        factor_str = " + ".join(map(str, result))
        print(f'{n} = {factor_str}')