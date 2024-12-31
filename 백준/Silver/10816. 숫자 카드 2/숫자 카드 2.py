from collections import Counter

N = int(input())
cards = list(map(int, input().split()))

M = int(input())
queries = list(map(int, input().split()))

card_count = Counter(cards)

result = [card_count[query] for query in queries]
print(*result)
