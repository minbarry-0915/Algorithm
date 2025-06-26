import sys

def cantor(n):
    if n == 0:
        return '-'
    prev = cantor(n - 1)
    return prev + ' ' * len(prev) + prev

for line in sys.stdin:
    if line.strip() == '':
        continue
    n = int(line.strip())
    print(cantor(n))
