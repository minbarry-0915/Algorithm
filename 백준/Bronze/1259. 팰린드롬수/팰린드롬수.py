while True:
    word = str(input()).rstrip()
    if word == '0':
        break
    if word == word[::-1]:
        print('yes')
    else:
        print('no')