import sys

# sys.stdin = open('input.txt', 'r', encoding='utf-8')

input = sys.stdin.readline
from collections import deque
def bfs(start, k):
    queue = deque()
    queue.append((start,0))
    visited = [{} for _ in range(k + 1)]
    max_num = -1

    while queue:
        num_str, cnt = queue.popleft()

        if cnt == k:
            max_num = max(max_num, int(num_str))
            continue

        m = len(num_str)

        for i in range(m):
            for j in range(i + 1, m):
                if i == 0 and num_str[j] == '0':
                    continue
                lst = list(num_str)
                lst[i], lst[j] = lst[j], lst[i]
                new_num = ''.join(lst)

                if new_num not in visited[cnt + 1]:
                    visited[cnt + 1][new_num] = True
                    queue.append((new_num, cnt + 1))

    return max_num

n,k = input().split()
k = int(k)

# 길이가 1, 길이가 2인데 0으로 시작
if len(n) == 1 or (len(n) == 2 and n[1] == '0' and k >= 1):
    print(-1)
else:
    print(bfs(n,k))