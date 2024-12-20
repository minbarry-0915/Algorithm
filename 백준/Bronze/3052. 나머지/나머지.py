total_set = set()

for _ in range(10):
    number = int(input())
    left = number % 42
    total_set.add(left)

print(len(total_set))