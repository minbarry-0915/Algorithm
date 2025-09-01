import heapq
def solution(n, s, a, b, fares):
    fares_graph = {i: [] for i in range(1, n + 1)}
    
    for c,d,f in fares:
        fares_graph[c].append([d,f])
        fares_graph[d].append([c,f])
        
    def get_djk(start):
        djk = [int(1e9)] * (n + 1)
        djk[start] = 0  # 출발점 비용 0

        heap = []
        heapq.heappush(heap, (0, start))  # (비용, 노드) 순서

        while heap:
            cost, current = heapq.heappop(heap)

            if cost > djk[current]:
                continue  # 이미 더 짧은 경로 존재

            for next_node, next_cost in fares_graph[current]:
                total_cost = cost + next_cost
                if total_cost < djk[next_node]:
                    djk[next_node] = total_cost
                    heapq.heappush(heap, (total_cost, next_node))

        return djk
                
    
    djk_s = get_djk(s)
    djk_a = get_djk(a)
    djk_b = get_djk(b)
    
    min_total_cost = int(1e9)
    # i = 합승 끝나는 지점
    for i in range(1, n + 1): 
        total_cost = djk_s[i] + djk_a[i] + djk_b[i]
        min_total_cost = min(min_total_cost, total_cost)

    return min_total_cost