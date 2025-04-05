import sys
input = sys.stdin.readline
from collections import deque

def distance(a,b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

t = int(input())
for _ in range(t):
    n = int(input()) #편의점 갯수
    places = [tuple(map(int, input().split())) for _ in range(n + 2)]

    graph = {i: [] for i in range(n + 2)} # 갈 수 있는 경로(간선) 그래프

    for i in range(n + 2):
        for j in range(n + 2):
            if i != j and distance(places[i], places[j]) <= 1000:
                graph[i].append(j)

    visited = [False] * (n + 2)

    queue = deque()
    queue.append(0)
    visited[0] = True

    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if not visited[next]:
                visited[next] = True
                queue.append(next)

    print("happy" if visited[-1] else "sad")