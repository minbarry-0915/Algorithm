

numbers = {
    1: None,
    2: ['A','B','C'],
    3: ['D','E','F'],
    4: ['G','H','I'],
    5: ['J','K','L'],
    6: ['M','N','O'],
    7: ['P','Q','R','S'],
    8: ['T','U','V'],
    9: ['W','X','Y','Z'],
    10: None,
}

def translate_code(code):
    solved = []
    for char in code:
        for key, value in numbers.items():
            if value and char in value:
                solved.append(key)
    return solved

if __name__ == '__main__':
    code = str(input().rstrip())
    real_code = translate_code(code)
    result = 0
    for digit in real_code:
        result += int(digit) + 1
    print(result)