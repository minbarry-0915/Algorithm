

s = list(input())
a = s.count('a')

s += s[0: a - 1]
min_val = int(1e9)

for i in range(len(s) - a + 1):
    min_val = min(min_val, s[i: i + a].count('b'))

print(min_val)