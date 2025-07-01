dx = [-1,1,0,0]
dy = [0,0,-1,1]
INF = int(1e9)
import heapq

problem = 1
while True:
    n = int(input())
    if n == 0:
        break

    grid = [list(map(int,input().split())) for _ in range(n)]
    costs = [[INF] * n for _ in range(n)]
    heap = []
    heapq.heappush(heap,(grid[0][0], 0,0)) # cost,x,y

    while heap:
        curr_cost, cx,cy = heapq.heappop(heap)
        if costs[cx][cy] < curr_cost:
            continue

        for d in range(4):
            nx,ny = cx + dx[d], cy + dy[d]
            if 0<= nx < n and 0 <= ny < n :
                next_cost = curr_cost + grid[nx][ny]
                if costs[nx][ny] > next_cost:
                    costs[nx][ny] = next_cost
                    heapq.heappush(heap, (next_cost, nx,ny))

    print(f'Problem {problem}: {costs[n-1][n-1]}')
    problem += 1