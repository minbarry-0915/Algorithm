N = int(input())

min_num = None

for i in range(1, N):
    num = i
    str_num = str(num)
    digits = [int(digit) for digit in str_num]
    if num + sum(digits) == N:
        if min_num is None or num < min_num:
            min_num = num

if min_num is None:
    print(0)
else:
    print(min_num)