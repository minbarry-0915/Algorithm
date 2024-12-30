digits = list(map(int, input().split()))

sum = 0
for digit in digits:
    sum += digit ** 2
result = sum % 10 
print(result)