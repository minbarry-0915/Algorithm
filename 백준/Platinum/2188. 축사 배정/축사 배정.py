def dfs(u):
    for v in adj[u]:
        if visited[v]:
            continue
        visited[v] = True
        if match[v] == 0  or dfs(match[v]): # 아직 매칭이 안되었거나, 매칭된 소가 다른 축사에 들어갈수 있는 경우
            match[v] = u
            return True
    return False

n,m = map(int,input().split())
adj = {i: [] for i in range(1, n + 1)}
for i in range(1, n + 1):
    buffer = list(map(int,input().split()))
    k = buffer[0]
    adj[i] = buffer[1:]

match = [0] * (m + 1)
cnt = 0

for cow in range(1,n + 1):
    visited = {i: False for i in range(1, m + 1)}
    if dfs(cow):
        cnt += 1

print(cnt)