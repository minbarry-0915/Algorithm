N, K = map(int, input().split())

# 초기 리스트 생성
people = list(range(1, N + 1))
result = []  # 요세푸스 순열을 저장할 리스트

index = 0  # 제거할 사람의 인덱스
while people:
    index = (index + K - 1) % len(people)  # K번째 사람의 인덱스 계산
    result.append(people.pop(index))  # 해당 인덱스의 사람을 제거하고 결과에 추가

# 결과 출력
print("<" + ", ".join(map(str, result)) + ">")
