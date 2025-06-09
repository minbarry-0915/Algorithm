import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
world = [list(map(int, input().split())) for _ in range(n)]
dp = {}


def DFS(now, visited):
    if visited == (1 << n) - 1:  # 모든 도시를 방문했을 경우
        if world[now][0]:  # 다시 출발 도시로 갈수 있는 경우
            return world[now][0]
        else:  # 갈수없으면 무한대
            return int(1e9)
    if (now, visited) in dp: # 이미 계산된 경우
        return dp[(now, visited)]

    min_cost = int(1e9)
    for next in range(1, n):
        if world[now][next] == 0 or visited & (1 << next):
            continue
        cost = DFS(next, visited | (1 << next)) + world[now][next]
        min_cost = min(cost, min_cost)

    dp[(now, visited)] = min_cost
    return min_cost


print(DFS(0, 1))
