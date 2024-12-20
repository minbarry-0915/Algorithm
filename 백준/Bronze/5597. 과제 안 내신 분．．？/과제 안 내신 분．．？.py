N = 30

my_dict = {i: False for i in range(1, N + 1)}
for _ in range(28):
    number = int(input())
    my_dict[number] = True

for key, value in my_dict.items():
    if not value:
        print(key)