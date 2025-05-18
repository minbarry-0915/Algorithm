# import sys

# sys.stdin = open('input.txt', 'r', encoding='UTF-8')
import heapq
def prim(n, islands, e):
    visited = [False] * n
    q = [(0,0)] # cost, index
    total_cost = 0
    cnt = 0

    while q:
        cost, u = heapq.heappop(q)
        if visited[u]:
            continue

        visited[u] = True
        total_cost += cost
        cnt += 1
        if cnt == n:
            break

        for v in range(n):
            if not visited[v]:
                dx = islands[u][0] - islands[v][0]
                dy = islands[u][1] - islands[v][1]
                dist = dx * dx + dy * dy
                heapq.heappush(q, (dist, v))

    return round(total_cost * e)

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    x_pos = list(map(int,input().split()))
    y_pos = list(map(int,input().split()))
    e = float(input())
    islands = [(x_pos[i],y_pos[i]) for i in range(n)]

    print(f'#{t} {prim(n, islands, e)}')