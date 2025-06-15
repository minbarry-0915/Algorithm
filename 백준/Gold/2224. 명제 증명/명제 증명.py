import sys
# sys.stdin = open('input.txt', 'r')

def char_to_index(c):
    if 'A' <= c <='Z':
        return ord(c) - ord('A')
    else:
        return ord(c) - ord('a') + 26

def index_to_char(i):
    if 0 <= i < 26:
        return chr(i + ord('A'))
    else:
        return chr(i - 26 + ord('a'))

n = int(input())
grid = [[False] * 52 for _ in range(52)]
for _ in range(n):
    a,b = input().split(' => ')
    u = char_to_index(a)
    v = char_to_index(b)
    grid[u][v] = True

for k in range(52):
    for i in range(52):
        for j in range(52):
            if grid[i][k] and grid[k][j]:
                grid[i][j] = True

result = []
for i in range(52):
    for j in range(52):
        if i != j and grid[i][j]:
            result.append((index_to_char(i), index_to_char(j)))
print(len(result))
for a, b in sorted(result):
    print(f"{a} => {b}")