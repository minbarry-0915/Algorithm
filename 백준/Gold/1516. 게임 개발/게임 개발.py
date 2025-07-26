n = int(input())

graph = {i:[] for i in range(1, n + 1)}
indegree = [0] * (n + 1)
times = [0] * (n + 1)
dp = [0] * (n + 1)


for i in range(1,n + 1):
    buffer = list(map(int,input().split()))
    times[i] = buffer[0]
    for node in buffer[1: -1]:
        graph[node].append(i)
        indegree[i] += 1

from collections import deque
q = deque()

for i in range(1, n + 1):
    if not indegree[i]:
        q.append(i)
        dp[i] = times[i]

while q:
    current = q.popleft()

    for next in graph[current]:
        indegree[next] -= 1
        dp[next] = max(dp[next], dp[current] + times[next])

        if not indegree[next] : q.append(next)

for i in range(1, n + 1):
    print(dp[i], end='\n')