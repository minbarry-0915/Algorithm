import sys
input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())
heights = list(map(int, input().split()))

# 이분 탐색 초기 범위 설정
low, high = 0, max(heights)
answer = 0

while low <= high:
    mid = (low + high) // 2  # 절단기 높이 설정
    total = sum(h - mid for h in heights if h > mid)  # 얻을 수 있는 나무 길이 계산

    if total >= M:  # 충분히 얻을 수 있으면 더 높은 절단기 시도
        answer = mid  # 정답 갱신
        low = mid + 1
    else:  # 부족하면 절단기 낮춤
        high = mid - 1

print(answer)  # 최대 절단기 높이 출력
