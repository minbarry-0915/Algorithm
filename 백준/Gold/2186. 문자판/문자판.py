import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n, m, k = map(int, input().split())
board = [list(input()) for _ in range(n)]
word = input().strip()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dp = [[[-1 for _ in range(len(word))] for _ in range(m)] for _ in range(n)]


def dfs(x, y, idx):
    if idx == len(word) - 1:
        return 1

    if dp[x][y][idx] != -1:
        return dp[x][y][idx]

    dp[x][y][idx] = 0
    for d in range(4):
        for step in range(1, k + 1):
            nx = x + dx[d] * step
            ny = y + dy[d] * step

            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == word[idx + 1]:
                dp[x][y][idx] += dfs(nx, ny, idx + 1)
    return dp[x][y][idx]


answer = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == word[0]:
            answer += dfs(i, j, 0)
print(answer)
