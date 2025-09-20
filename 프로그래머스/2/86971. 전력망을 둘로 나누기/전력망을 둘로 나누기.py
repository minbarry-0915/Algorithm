from collections import deque
def solution(n, wires):
    answer = int(1e9)
    ## 모든 전선을 끊어봐서 diff 가 가장 작은 경우의 수를 찾아야됨
    graph = {i : [] for i in range(1,n + 1)}
    for [a,b] in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    def bfs(start, cutting_edge):
        queue = deque()
        visited = {i: False for i in range(1, n + 1)}
        queue.append(start)
        visited[start] = True
        count = 1
        
        while queue:
            current = queue.popleft()
            
            for next in graph[current]:
                if not visited[next] and not ([current,next] == cutting_edge or [next, current] == cutting_edge):
                    visited[next] = True
                    queue.append(next)
                    count += 1
        return count
    
    # 하나씩 다 끊어보기
    for [a,b] in wires:
        count1 = bfs(a, [a,b])
        count2 = n - count1
        diff = abs(count1 - count2)
        answer = min(answer, diff)
    return answer