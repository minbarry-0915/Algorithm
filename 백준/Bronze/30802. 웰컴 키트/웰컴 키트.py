N = int(input())  # 총 입력 개수
counts = list(map(int, input().split()))  # 각 개수를 리스트로 저장
T, P = map(int, input().split())  # 기준 값 T와 P

# 1. T 기준으로 계산
total_T = 0
for count in counts:
    total_T += count // T  # T에 맞춰 나눈 몫 더하기
    if count % T > 0:  # 나머지가 있으면 추가 1번 더 필요
        total_T += 1

# 2. P 기준으로 계산
total_P = sum(counts)  # 전체 개수의 합
dozen_P = total_P // P  # P 단위의 몫
remain_P = total_P % P  # 나머지

# 결과 출력
print(total_T)
print(dozen_P, remain_P)
