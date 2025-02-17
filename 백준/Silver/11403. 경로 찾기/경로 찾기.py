#경로 찾기
import sys
sys.setrecursionlimit(10 * 6)
input = sys.stdin.readline

n= int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1
                
for row in graph:
    print(*row)