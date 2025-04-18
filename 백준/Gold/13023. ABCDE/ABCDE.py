import sys
#sys.stdin = open('input.txt','r')

sys.setrecursionlimit(10 ** 6)
def dfs(idx, depth):
    global found
    if depth == 5:
        found = 1
        return

    # 답을 하나만 찾아도 될 경우에 외부 백 트랙킹 사용
    visited[idx] = 1
    for neighbor in graph[idx]:
        if not visited[neighbor]:
            dfs(neighbor, depth + 1)
            if found:
                return
    visited[idx] = 0

n, m = map(int, input().split())
graph = {i: [] for i in range(n)}
visited = [0] * n
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

found = 0
for i in range(n):
    dfs(i, 1)
    if found:
        break

print(found)
