X = int(input())

# 대각선 번호(n) 찾기
n = 1
sum_ = 0

while True:
    sum_ += n  # n번째 대각선까지의 총 분수 개수
    if sum_ >= X:
        break
    n += 1

# X가 해당 대각선의 몇 번째 위치인지 계산
difference = sum_ - X  # 대각선의 끝에서 X까지의 거리
position = n - difference  # 대각선 내의 위치 (1부터 시작)

# 분모와 분자 계산
if n % 2 == 0:  # 짝수 대각선 (아래에서 위로)
    numerator = position
    denominator = n - position + 1
else:  # 홀수 대각선 (위에서 아래로)
    numerator = n - position + 1
    denominator = position

print(f"{numerator}/{denominator}")
