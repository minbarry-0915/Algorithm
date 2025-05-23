T = int(input())

def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def dfs(idx, depth, visited, dist_sum, n):
    global min_dist
    if depth == n:
        dist_sum += manhattan(customers[idx], home)
        min_dist = min(min_dist, dist_sum)
        return

    if dist_sum >= min_dist:
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(i, depth + 1, visited, dist_sum + manhattan(customers[idx], customers[i]), n)
            visited[i] = False

for t in range(1, T + 1):
    n = int(input())
    buffer = list(map(int, input().split()))
    company = (buffer[0], buffer[1])
    home = (buffer[2], buffer[3])
    customers = [(buffer[i], buffer[i + 1]) for i in range(4, len(buffer), 2)]

    min_dist = int(1e9)
    visited = [False] * n

    for i in range(n):
        visited[i] = True
        dfs(i, 1, visited, manhattan(company, customers[i]), n)
        visited[i] = False

    print(f'#{t} {min_dist}')