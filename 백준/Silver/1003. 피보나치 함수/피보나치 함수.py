import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    DP = [[]] * 41
    DP[0] = [1, 0]
    DP[1] = [0, 1]
    DP[2] = [1, 1]

    for i in range(3, N + 1):
        DP[i] = [DP[i - 1][0] + DP[i - 2][0], DP[i - 1][1] + DP[i - 2][1]]

    print(DP[N][0], DP[N][1])
