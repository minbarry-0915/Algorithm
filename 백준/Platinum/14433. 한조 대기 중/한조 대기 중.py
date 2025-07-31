def max_match(n,m,adj):
    match = [0] * (m + 1)

    def dfs(u):
        for v in adj[u]:
            if visited[v]:
                continue
            visited[v] = True
            if match[v] == 0 or dfs(match[v]):
                match[v] = u
                return True
        return False

    cnt = 0
    for u in range(1, n + 1):
        visited = [False] * (m + 1)
        if dfs(u): cnt += 1
    return cnt

n,m,k1,k2 = map(int,input().split())
adj1 = [[] for _ in range(n + 1)]
adj2 = [[] for _ in range(n + 1)]

for _ in range(k1):
    u,v = map(int,input().split())
    adj1[u].append(v)
for _ in range(k2):
    u,v = map(int,input().split())
    adj2[u].append(v)

cnt1 = max_match(n,m,adj1)
cnt2 = max_match(n,m,adj2)
print('네 다음 힐딱이' if cnt1 < cnt2 else '그만 알아보자')