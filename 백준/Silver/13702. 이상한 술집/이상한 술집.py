import sys

input = sys.stdin.readline

# 입력 받기
n, k = map(int, input().split())
capacities = [int(input()) for _ in range(n)]

# 이분 탐색 범위 설정
left, right = 1, max(capacities)
answer = 0  # 최대 분배량 저장

while left <= right:
    mid = (left + right) // 2  # 중간값 (술 한 명당 배분할 양)
    count = sum(capacity // mid for capacity in capacities)  # mid만큼 나눌 수 있는 인원 계산

    if count >= k:
        answer = mid  # 가능한 경우, 더 큰 값을 탐색
        left = mid + 1
    else:
        right = mid - 1

print(answer)
