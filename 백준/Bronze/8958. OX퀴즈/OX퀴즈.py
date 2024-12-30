T = int(input())
for testCase in range(1, T + 1):
    logs = str(input())

    score = 0
    sequential = 0
    i = 0
    for char in logs:
        if char == 'O':
            sequential += 1
            score += sequential
        else:
            sequential = 0
    print(score)
