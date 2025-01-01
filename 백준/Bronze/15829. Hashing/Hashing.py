L = int(input())
word = str(input())
r = 31
M = 1234567891
H = 0

for i in range(L):
    temp = (ord(word[i]) - ord('a') + 1) * (r ** i)
    H += temp

result = H % M
print(result)