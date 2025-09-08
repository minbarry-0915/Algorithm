n,m = map(int,input().split())
# 0: 안보임 1: 보임, 마지막 인덱스는 상대넥서스여서 보이지만 갈 수 있음
visibility = list(map(int,input().split()))
graph = {i: [] for i in range(n)} # 0-based

for _ in range(m):
  a,b,t = map(int,input().split())
  graph[a].append((b,t))
  graph[b].append((a,t))
  
import heapq
heap = []
INFINITY = 10 ** 14
costs = [INFINITY] * n
costs[0] = 0
heapq.heappush(heap, (0, 0)) # cost, node

while heap:
  cost, node = heapq.heappop(heap)
  
  if costs[node] < cost: # 이미 최소 경로
    continue
  
  for next_node, next_cost in graph[node]:
    total_cost = cost + next_cost
    # 상대의 시야 이고, 상대 넥서스가 아니면 -> 갈수 없음
    if visibility[next_node] == 1 and next_node != n - 1:
      continue
    if total_cost < costs[next_node]:
      costs[next_node] = total_cost
      heapq.heappush(heap, (total_cost, next_node))

print(costs[n - 1] if costs[n - 1] != INFINITY else -1)