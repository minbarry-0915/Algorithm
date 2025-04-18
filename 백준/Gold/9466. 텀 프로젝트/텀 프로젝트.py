import sys
# sys.stdin = open('input.txt','r')
sys.setrecursionlimit(10 ** 6)
def dfs(node):
    global count
    visited[node] = True
    next_node = lst[node]

    if not visited[next_node]:
        dfs(next_node)
    else:
        # 방문한적 있는데
        if not done[next_node]:
            cur = next_node
            while cur != node:
                count += 1
                cur = lst[cur]
            count += 1 # node 자기 자신도 추가

    done[node] = True
t = int(input())
for _ in range(t):
    n = int(input())
    count = 0 # 사이클에 포함되어있는 노드의 갯수
    lst = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)
    done = [False] * (n + 1)  # 사이클 탐지 여부

    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)
    print(n - count)