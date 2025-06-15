import sys
from collections import deque
from itertools import combinations

# sys.stdin = open('input.txt','r')

n = int(input())
population = [0] + list(map(int,input().split()))
graph ={i: [] for i in range(1, n + 1)}

for i in range(1,n + 1):
    tmp = list(map(int,input().split()))
    graph[i] = tmp[1:]

def get_combinations(nodes):
    results = []
    length = len(nodes)
    for i in range(1, length // 2 + 1):
        for comb in combinations(nodes, i):
            rest = tuple(set(nodes) - set(comb))
            results.append((comb, rest))
    return results

def bfs(area):
    s = area[0]
    queue = deque([s])
    visited = set([s])
    cost = 0

    while queue:
        v = queue.popleft()
        cost += population[v]

        for node in graph[v]:
            if node in area and node not in visited:
                visited.add(node)
                queue.append(node)

    # 연결 여부 확인
    if len(visited) != len(area):
        return -1
    return cost

result = int(1e9)
nodes = tuple(range(1, n + 1))

for area in get_combinations(nodes):
    a_cost = bfs(area[0])
    b_cost = bfs(area[1])

    if a_cost == -1 or b_cost == -1:
        continue

    result = min(result, abs(a_cost - b_cost))

print(-1 if result == int(1e9) else result)