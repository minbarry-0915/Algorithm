def get_exp(num, exp):
    if exp == 0:
        return 1
    return num * get_exp(num, exp - 1)


for _ in range(10):
    t = int(input())
    num, exp = map(int, input().split())
    result = get_exp(num, exp)
    print(f'#{t} {result}')