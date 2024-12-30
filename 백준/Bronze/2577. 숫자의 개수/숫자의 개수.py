A = int(input())
B = int(input())
C = int(input())

sum = str(A * B * C)

counter = {str(i): 0 for i in range(10)}

for digit in sum:
    counter[digit] += 1
    
for value in counter.values():
    print(value)