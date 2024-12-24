T = int(input())
for testcase in range(1, T + 1):
    R, S = map(str, input().split())
    R = int(R)

    result = ''.join([char * R for char in S])
    print(result)