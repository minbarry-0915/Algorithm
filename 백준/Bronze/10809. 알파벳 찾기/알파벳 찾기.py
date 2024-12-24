S = str(input())

alphabet = 'abcdefghijklmnopqrstuvwxyz'

result = [S.find(char) for char in alphabet]
print(' '.join(map(str, result)))