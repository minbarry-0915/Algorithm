from collections import deque

def find_min_time(N, K):
    # 최대 100,000까지의 위치를 고려해야 하므로 배열의 크기를 100,001로 설정
    MAX = 100000
    # 방문 여부를 체크할 배열
    visited = [False] * (MAX + 1)
    # 큐 초기화: (위치, 시간)
    queue = deque([(N, 0)])
    visited[N] = True

    while queue:
        current, time = queue.popleft()

        # 동생의 위치에 도달한 경우
        if current == K:
            return time

        # 이동할 수 있는 위치들: 걷기 (X-1, X+1), 순간이동 (2*X)
        for next_pos in [current - 1, current + 1, current * 2]:
            if 0 <= next_pos <= MAX and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, time + 1))

# 입력 받기
N, K = map(int, input().split())

# 결과 출력
print(find_min_time(N, K))
