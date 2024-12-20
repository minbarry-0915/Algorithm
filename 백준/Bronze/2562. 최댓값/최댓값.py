A = []
for i in range(9):
    A.append(int(input()))

max_value = max(A)  # 최댓값 구하기
max_index = A.index(max_value) + 1  # 최댓값의 위치 (1-based index)

print(max_value)  # 최댓값 출력
print(max_index)  # 최댓값 위치 출력
