from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
data = []
_sum = 0
count = dict()

for _ in range(N):
    x = int(input())
    data.append(x)

    _sum += x

    if x not in count:
        count[x] = 1
    else:
        count[x] += 1

data.sort()

print(round(_sum / N))

print(data[N // 2])

freq = max(count.values())
numbers = []
for key, value in count.items():
    if value == freq:
        numbers.append(key)

if len(numbers) == 1:
    print(numbers[0])
else:
    print(sorted(numbers)[1])

print(data[-1] - data[0])