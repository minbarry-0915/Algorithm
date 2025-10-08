import sys
from collections import defaultdict

# sys.stdin = open('input.txt','r')

n = int(input())
words = list(input() for _ in range(n))

# 알파벳을 숫자로 변환해서 알파벳으로 이뤄진 단어들의 최대합을 구하라
# 숫자 배치 전략
# 가중치를 줘야됨: 자릿값에서 몇 번 등장했는가?

weights = defaultdict(int)

for word in words:
    length = len(word)
    for i, ch in enumerate(word):
        weights[ch] += 10 ** (length - i - 1)

sorted_weights = sorted(weights.items(), key=lambda x: -x[1]) # 가중치가 큰 순

# 9부터 부여
digit = 9
mapping = {}
for ch, _ in sorted_weights:
    mapping[ch] = digit
    digit -= 1

total = 0
for word in words:
    num_str = ''.join(str(mapping[ch]) for ch in word)
    total += int(num_str)
print(total)