from collections import deque

def solution(n, computers):
    graph = {i: [] for i in range(n)}
    
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if computers[i][j]:
                graph[i].append(j)
                graph[j].append(i)
            
    def bfs(start, visited):
        queue = deque()
        queue.append(start)
        visited[start] = True

        while queue:
            curr = queue.popleft()
            for next in graph[curr]:
                if not visited[next]:
                    visited[next] = True
                    queue.append(next)     
        return 1
    
    result = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            result += bfs(i, visited)
    return result
            

    


    
    
    
    