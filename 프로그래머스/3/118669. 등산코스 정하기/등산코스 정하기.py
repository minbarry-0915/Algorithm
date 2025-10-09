import heapq

INF = int(1e9)
def solution(n, paths, gates, summits):
    graph = {i: [] for i in range(1, n + 1)}
    
    for i,j,cost in paths:
        graph[i].append((j,cost))
        graph[j].append((i,cost))
    # 산봉우리 검색 최적화
    is_summit = {i: False for i in range(1, n + 1)}
    for s in summits:
        is_summit[s] = True
    
    # 산봉우리 1개를 찍고, 다시 줄발점으로 돌아오는 코스: 편도 처리
    # dijkstra 알고리즘
    dist = [INF] * (n + 1)
    heap = []
    # 출발점은 intensity 0
    for g in gates:
        dist[g] = 0
        heapq.heappush(heap, (0,g))
    
    while heap:
        intensity, curr = heapq.heappop(heap)
        # 산봉우리거나 이미 intensity가 더 작으면 더이상 탐색할 필요없음
        if dist[curr] < intensity or is_summit[curr]: 
            continue
            
        for nxt, cost in graph[curr]:
            new_intensity = max(intensity, cost)
            # 새로운 최소 intensity 발견
            if new_intensity < dist[nxt]:
                dist[nxt] = new_intensity
                heapq.heappush(heap,(new_intensity, nxt))
    
    result = [-1,INF]
    for s in sorted(summits):
        if dist[s] < result[1]:
            result = [s, dist[s]]
    return result