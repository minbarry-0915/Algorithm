from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))

max_sum = 0
for comb in combinations(cards, 3):
    total = sum(comb)
    if total <= M:
        max_sum = max(max_sum, total)
        
print(max_sum)