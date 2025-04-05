import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())

def bfs(n, k):
    visited = [0] * 100001
    queue = deque()
    queue.append(n)

    while queue:
        current = queue.popleft()

        if current == k:
            return visited[current]

        for next_pos in [current -1 ,current + 1, current * 2]:
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = visited[current] + 1
                queue.append(next_pos)

print(bfs(n,k))