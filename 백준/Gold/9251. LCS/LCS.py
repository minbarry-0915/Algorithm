
def lcs(x, y):
    global dp
    x, y = ' ' + x, ' ' + y
    for i in range(1, len(x)):
        for j in range(1, len(y)):
            if x[i] == y[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[len(x) - 1][len(y) - 1]


word1 = input()
word2 = input()

dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
print(lcs(word1, word2))