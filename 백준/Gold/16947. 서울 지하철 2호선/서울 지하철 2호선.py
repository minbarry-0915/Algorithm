import sys
sys.setrecursionlimit(10**4)

n = int(input())
graph = {i: [] for i in range(1, n+1)}
for _ in range(n):
  a,b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [False]*(n+1)
on_cycle = [False]*(n+1)

def dfs(curr, prev):
  visited[curr] = True
  for nxt in graph[curr]:
    if nxt == prev: # 다음 지점이 바로 직전에 갔던 지점 -> 사이클 성립안됨
      continue
    if visited[nxt]: # 다음 지점이 재방문일 경우 -> 사이클임
      on_cycle[curr] = True # 현재 노드는 사이클의 일부가 됨
      return nxt # 사이클의 시작점 반환
    res = dfs(nxt, curr)
    if res != -1:  # 사이클의 시작지점이 있는 경우
      on_cycle[curr] = True # 현재 노드는 사이클의 일부가 됨
      if curr == res: # 재귀를 통해 알아온 사이클의 시작지점이 나 자신이면
        return -1 # 사이클 끝
      else: # 사이클의 시작지점은 있는데 나는 아님
        return res # 위로 계속 전달
  return -1

from collections import deque
def bfs(start):
  queue = deque()
  visited = [-1] * (n + 1)
  queue.append(start)
  visited[start] = 0
  
  while queue:
    curr = queue.popleft()
    if on_cycle[curr]:
      return visited[curr]
    for nxt in graph[curr]:
      if visited[nxt] == -1:
        visited[nxt] = visited[curr] + 1
        queue.append(nxt)
  return -1
    
dfs(1, -1)



dist = [0] * (n + 1)
for i in range(1, n + 1):
  if not on_cycle[i]:
    dist[i] = bfs(i)
print(' '.join(map(str,dist[1:])))