import heapq
T = int(input())
for _ in range(T):
    n,d,c = map(int,input().split())
    graph = {i: [] for i in range(1, n + 1)}
    for _ in range(d):
        a,b,s = map(int,input().split())
        graph[b].append((a,s))

    costs = [int(1e9)] * (n + 1)
    costs[c] = 0
    heap = []
    heapq.heappush(heap, (0, c))
    while heap:
        curr_cost, curr_node = heapq.heappop(heap)

        if costs[curr_node] < curr_cost:
            continue

        for neighbor, cost in graph[curr_node]:
            next_cost = curr_cost + cost
            if next_cost < costs[neighbor]:
                costs[neighbor] = next_cost
                heapq.heappush(heap, (next_cost, neighbor))

    count = sum(cost != int(1e9) for cost in costs[1:])
    time = max(cost for cost in costs[1:] if cost != int(1e9))
    print(count, time)
