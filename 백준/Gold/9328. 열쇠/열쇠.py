import sys
# sys.stdin = open('input.txt','r')

from collections import deque

T = int(input())

results = []

for _ in range(T):

    h, w = map(int, input().split())

    # 입력

    graph = []

    graph.append(["." for _ in range(w + 2)])

    for _ in range(h):
        graph.append(list("." + input() + "."))

    graph.append(["." for _ in range(w + 2)])

    keys = [0 for _ in range(26)]  # a~z : 0 초기화

    for k in list(input()):

        if k != "0":
            keys[ord(k) - 97] = 1

    # BFS

    dr = [1, 0, -1, 0]

    dc = [0, 1, 0, -1]

    deq = deque([(0, 0)])

    papers = 0

    tempDoors = [[] for _ in range(26)]  # A~Z : [] 초기화

    while deq:

        r, c = deq.popleft()

        # 상하좌우 방문 확인 및 queue append

        for i in range(4):

            nr = r + dr[i]

            nc = c + dc[i]

            if 0 <= nr < h + 2 and 0 <= nc < w + 2 and graph[nr][nc] != "*":

                # 방문 처리 및 방문한 곳의 상태에 대한 업데이트

                num = ord(graph[nr][nc])

                if 65 <= num <= 90:  # 문

                    # 열쇠가 없는 상태면, 문을 임시 저장

                    if keys[num - 65] == 0:
                        tempDoors[num - 65].append((nr, nc))

                        continue

                elif 97 <= num <= 122:  # 열쇠

                    # 열쇠가 새로 추가된다면, 임시 저장한 문을 꺼내 deq 맨 위에 push

                    if keys[num - 97] == 0:

                        for door in tempDoors[num - 97]:
                            deq.appendleft(door)

                    keys[num - 97] = 1

                elif graph[nr][nc] == "$":  # 서류

                    papers += 1

                graph[nr][nc] = "*"

                deq.append((nr, nc))

    results.append(papers)

for r in results:
    print(r)