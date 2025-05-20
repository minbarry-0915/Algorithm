T = int(input())

for t in range(1,T + 1):
    n = int(input())
    parent = {i: 0 for i in range(1, n + 1)}
    for _ in range(n - 1):
        a,b = map(int, input().split())
        parent[b] = a

    u,v = map(int,input().split())

    # u의 모든 조상을 set에 저장
    ancestors = set()
    while u:
        ancestors.add(u)
        u = parent[u]

    # v의 조상을 루트까지 거슬러가며 u의 조상과 처음 만나는 지점 찾기
    while v:
        if v in ancestors:
            print(v)
            break
        v = parent[v]