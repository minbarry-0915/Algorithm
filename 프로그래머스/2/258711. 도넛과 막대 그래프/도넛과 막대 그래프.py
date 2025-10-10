from collections import defaultdict
def solution(edges):
    graph = defaultdict(list)
    indegree = defaultdict(int)
    outdegree = defaultdict(int)
    
    for u,v in edges:
        graph[u].append(v)
        outdegree[u] += 1
        indegree[v] += 1
        
        if not outdegree[v]:
            outdegree[v] = 0
        if not indegree[u]:
            indegree[u] = 0
 
    n = len(indegree.keys())
    
    # 중심, 막대기, 8자 탐색
    center = -1
    stick_count = 0
    eight_count = 0
    doughnut_count = 0
    for i in range(1, n + 1):
        if outdegree[i] >= 2 and indegree[i] == 0:
            center = i
        elif outdegree[i] == 0 and indegree[i] >= 1: 
            stick_count += 1
        elif outdegree[i] >= 2 and indegree[i] >= 2:
            eight_count += 1
    doughnut_count = outdegree[center] - stick_count - eight_count
    answer = [center, doughnut_count, stick_count, eight_count]
    print(answer)
    return answer