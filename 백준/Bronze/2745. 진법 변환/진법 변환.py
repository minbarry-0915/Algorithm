N, B = map(str, input().split())
B = int(B)

def convert_to_decimal(N, B):
    decimal_value = 0
    power = 0

    for digit in reversed(N):
        if '0' <= digit <= '9':
            value = ord(digit) - ord('0')
        else:
            value = ord(digit) - ord('A') + 10
        decimal_value += value * (B ** power)
        power += 1
    return decimal_value

print(convert_to_decimal(N, B))