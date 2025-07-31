def dfs(u):
    for v in adj[u]:
        if not visited[v]:
            visited[v] = True
            # 매칭한 사람이 없는 일 or 매칭된사람이 다른 일로 바꿀수있는경우
            if match[v] == 0 or dfs(match[v]):
                match[v] = u # 연결
                return True
    return False


n,m = map(int,input().split())
adj = {i: [] for i in range(1, n + 1)}

for i in range(1, n + 1):
    buffer = list(map(int,input().split()))
    k = buffer[0] # 할일의 갯수
    adj[i] = buffer[1:] # 할일의 번호들

match = [0] * (m + 1) # 현재 직원 - 일 매칭 상태
cnt = 0 # 매칭 갯수

for num in range(1, n + 1):
    visited = [False] * (m + 1)
    if dfs(num):
        cnt += 1
print(cnt)