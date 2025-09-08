g, ss = map(int, input().split())
w = list(input().strip())
s = list(input().strip())

from collections import defaultdict

looking_for = defaultdict(int)
for ch in w:
  looking_for[ch] += 1

window = defaultdict(int)
for ch in s[0: g]:
  window[ch] += 1

count = 0
if looking_for == window:
  count += 1
  

# 윈도우 탐색 진행
for i in range(ss - g):
  window[s[i]] -= 1
  window[s[i + g]] += 1
  if window[s[i]] == 0:
    del window[s[i]]
  if window == looking_for:
    count += 1
print(count)  
