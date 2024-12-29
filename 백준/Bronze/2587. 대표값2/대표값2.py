numbers = []
for _ in range(5):
    number = int(input())
    numbers.append(number)

numbers.sort()
average = sum(numbers) // len(numbers)
print(average)
print(numbers[2])