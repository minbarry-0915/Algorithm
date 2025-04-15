import sys
sys.setrecursionlimit(10 ** 6)
def find(x):  # x의 루트를 찾아라
    if parent[x] == x:  # 루트가 자기자신이면 끝
        return x
    parent[x] = find(parent[x])  # 루프돌면서 루트를 찾아감
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


v, e = map(int,input().split())  # 노드, 간선 갯수
parent = [i for i in range(v + 1)]  # 부모정보 저장
edges = []  # 간선 정보 저장
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort(key=lambda x: x[0])  # cost 순으로 정렬

total_cost = 0
for cost, a, b in edges:
    if find(a) != find(b):  # a,b 가 간선으로 연결되어있으나 루트가 같지 않음
        # 연결 진행
        union(a,b)
        total_cost += cost
print(total_cost)