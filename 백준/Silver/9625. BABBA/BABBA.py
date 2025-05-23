k = int(input())
# a: 1 b: 0
# a: 0 b: 1
# a: 1 b: 1
# a: 1 b: 2
# a: 2 b: 3
a,b = 1, 0
for _ in range(k):
    a,b = b, a + b
print(a, b)