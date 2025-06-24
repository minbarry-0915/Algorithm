n,k = map(int,input().split())

# 어떤 단어든 anta tica => [a,n,t,i,c] 는 무조건 포함

from itertools import combinations

if k < 5:
    print(0)
    exit()

essential = {'a','n','t','i','c'}

word_sets = []
all_chars = set()

for _ in range(n):
    # 배워야되는 단어
    word = set(input().strip()[4:-4]) - essential
    word_sets.append(word)
    all_chars.update(word)

candidates = list(all_chars)
selectable_count = min(k - 5, len(candidates))

max_count = 0

for comb in combinations(candidates, selectable_count):
    learned = set(essential) | set(comb)

    # 필수단어제외한 단어 집합이 배워야하는 단어의 부분집합인 경우 -> 배울수있음!
    count = sum(1 for word in word_sets if word <= learned)
    max_count = max(max_count, count)

print(max_count)