import sys
# sys.stdin = open('input.txt','r', encoding='utf-8')
input = sys.stdin.readline


def findPrime():
    for i in range(2, 100):
        if prime[i] == True:
            for j in range(2 * i, 10000, i):
                prime[j] = False

from collections import deque

def bfs(start, target):
    queue = deque()
    queue.append([start,0])

    visited = [False for i in range(10000)]
    visited[start] = True

    while queue:
        now, cnt = queue.popleft()
        str_now = str(now)

        if now == target:
            return cnt

        for i in range(4):
            for j in range(10):
                temp = int(str_now[:i] + str(j) + str_now[i + 1:])

                if not visited[temp] and prime[temp] and temp >= 1000:
                    visited[temp] = True
                    queue.append([temp, cnt + 1])


T = int(input())
prime = [True for _ in range(10000)]
findPrime()

for _ in range(T):
    start, target = map(int,input().split())
    answer = bfs(start, target)

    print(answer if answer != None else 'Impossible')