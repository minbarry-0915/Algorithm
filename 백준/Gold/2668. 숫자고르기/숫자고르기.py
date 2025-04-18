def dfs(v, start):
    visited[v] = True
    next_node = data[v]

    if not visited[next_node]:
        dfs(next_node, start)
    elif next_node == start:
        result.append(start)

n = int(input())
data = [0] + [int(input()) for _ in range(n)]  # 1-indexed
result = []

for i in range(1, n + 1):
    visited = [False] * (n + 1)
    dfs(i, i)

print(len(result))
for num in sorted(result):
    print(num)
