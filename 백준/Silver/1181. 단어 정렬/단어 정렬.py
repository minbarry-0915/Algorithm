N = int(input())
words = [input().strip() for _ in range(N)]
words = set(words)

words = list(words)
words.sort(key = lambda x: (len(x), x))

for word in words:
    print(word)