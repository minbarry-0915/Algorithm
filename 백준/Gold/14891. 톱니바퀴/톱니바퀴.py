import sys
from collections import deque

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

chains = [input().strip() for _ in range(4)]
k = int(input())
commands = [tuple(map(int, input().split())) for _ in range(k)]

def make_deque(chain):
    queue = deque()
    for i in range(len(chain)):
        queue.append(chain[i])
    return queue

chains_deque = [make_deque(chain) for chain in chains]

def update(chain_idx, direction):  # -1: 반시계 방향, 1: 시계 방향
    global chains_deque
    if direction == -1:
        element = chains_deque[chain_idx].popleft()
        chains_deque[chain_idx].append(element)
    elif direction == 1:
        element = chains_deque[chain_idx].pop()
        chains_deque[chain_idx].appendleft(element)
    else: # 0일 때
        return



def get_direction(chain_idx, direction):
    directions = [0, 0, 0, 0]
    directions[chain_idx] = direction

    # 바꾼 인덱스 기준 왼쪽 (연쇄로 적용)
    for i in range(chain_idx - 1, -1, -1):
        # 같지 않은 경우
        if chains_deque[i][2] != chains_deque[i + 1][-2]:
            # 해당 톱니바퀴의 반대 방향으로 감 
            directions[i] = -directions[i + 1]
        else: # 같으면 돌지 않으므로 0으로 유지
            break
    # 바꾼 인덱스 기준 오른족
    for i in range(chain_idx + 1, 4):
        if chains_deque[i - 1][2] != chains_deque[i][-2]:
            directions[i] = -directions[i - 1]
        else:
            break
    return directions

for chain_idx, direction in commands:
    directions = get_direction(chain_idx - 1, direction)
    for i in range(4):
        update(i, directions[i])

score = 0
for i in range(4):
    if chains_deque[i][0] == '1':
        score += 2 ** i
print(score)