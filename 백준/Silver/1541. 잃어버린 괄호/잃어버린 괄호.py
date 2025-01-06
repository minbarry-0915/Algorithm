import re
expression = input()

parts = expression.split('-')

initial_sum = sum(map(int, parts[0].split('+')))

result = initial_sum
for part in parts[1:]:
    result -= sum(map(int, part.split('+')))

print(result)