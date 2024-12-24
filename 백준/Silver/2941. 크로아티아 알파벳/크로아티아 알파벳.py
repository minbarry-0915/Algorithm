words = str(input())
count = 0

crot = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

i = 0
while i < len(words):
    if i + 1 < len(words) and words[i:i+2] in crot:
        count += 1
        i = i + 2
    elif i + 2 < len(words) and words[i:i+3] in crot:
        count += 1
        i = i + 3
    else:
        count += 1
        i += 1
print(count)