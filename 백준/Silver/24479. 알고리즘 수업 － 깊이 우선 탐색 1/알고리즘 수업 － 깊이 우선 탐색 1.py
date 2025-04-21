import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m, r = map(int, input().split())  # 정점의 수, 간선의 수, 시작 정점
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)  # 방문 순서 저장. 0이면 방문 X

c = 1


def dfs(graph, v, visited):
    global c
    visited[v] = c  # 방문하면 순서 나타내기

    for i in graph[v]:
        if visited[i] == 0:  # 방문 안한 노드이면
            c += 1
            dfs(graph, i, visited)  # dfs 재귀


# m개의 연결된 간선 정보 입력받기
for i in range(m):
    a, b = (map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

for i in range(n + 1):  # 오름차순으로 인접노드 방문하기 위해 정렬
    graph[i].sort()
# print(graph)

dfs(graph, r, visited)

for i in range(1, n + 1):
    print(visited[i])