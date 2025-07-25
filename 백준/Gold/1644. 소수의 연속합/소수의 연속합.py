def get_primes_up_to(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i): # i의 제곱들은 prime 이 아님
                is_prime[j] = False

    return [i for i, val in enumerate(is_prime) if val]

n = int(input())
primes = get_primes_up_to(n)
start = 0
end = 0
total = 0
answer = 0

while True:
    if total == n:
        answer += 1

    if total >= n:
        total -= primes[start]
        start += 1
    elif end == len(primes):
        break
    else:
        total += primes[end]
        end += 1

print(answer)