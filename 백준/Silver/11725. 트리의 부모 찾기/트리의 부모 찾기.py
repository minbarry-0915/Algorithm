import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graph, parent, node):
    for neighbor in graph[node]:
        if parent[neighbor] == -1:  # 아직 부모가 설정되지 않은 경우
            parent[neighbor] = node  # 현재 노드를 부모로 설정
            dfs(graph, parent, neighbor)

# 입력 받기
N = int(input())  # 노드의 개수
graph = [[] for _ in range(N + 1)]  # 그래프 초기화 (1-based index)

# 트리의 간선 정보 입력 받기
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 부모 정보를 저장할 배열
parent = [-1] * (N + 1)  # 부모를 기록할 배열, -1은 아직 부모가 설정되지 않은 상태
parent[1] = 0  # 루트의 부모는 0 (없음)

# DFS 탐색
dfs(graph, parent, 1)

# 부모 정보 출력
for i in range(2, N + 1):
    print(parent[i])