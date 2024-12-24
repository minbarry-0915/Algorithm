from collections import Counter

word = str(input().lower())

counter = Counter(word)

max_count = max(counter.values())

most_common = [key for key, value in counter.items() if value == max_count]
if len(most_common) > 1:
    print('?')
else:
    print(most_common[0].upper())