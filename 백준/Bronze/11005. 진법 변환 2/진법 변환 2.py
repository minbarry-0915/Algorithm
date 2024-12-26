N, B = map(int, input().split())

def convert_to_base(N, B):
    result = []
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if N == 0:
        return "0"

    while N > 0:
        result.append(digits[N % B])
        N = N // B

    return ''.join(reversed(result))

print(convert_to_base(N, B))