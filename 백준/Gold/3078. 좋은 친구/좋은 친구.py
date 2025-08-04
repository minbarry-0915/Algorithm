
n,k = map(int,input().split())
names = [input().strip() for _ in range(n)]
from collections import deque

length_queues = {}
answer = 0
for i in range(n):
    length = len(names[i])
    if length not in length_queues:
        length_queues[length] = deque()
    q = length_queues[length]
    
    
    while q and i - q[0] > k:
        q.popleft()
    
    answer += len(q)
    q.append(i)
    
print(answer)