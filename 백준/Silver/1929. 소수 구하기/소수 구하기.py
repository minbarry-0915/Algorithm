M,N = map(int,input().split())

#2개의 자연수 입력
#2개의 자연수 이상, 이하값을 하나씩 확인
#1은 소수에서 제외
# 2 ~ 제곱근 사이 나누어떨어진다면 종료
#나누어 떨어지지 않으면 출력

for i in range(M, N + 1):
    if i == 1:
        continue
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0: #분해가 되면 합성수임
            break
    else:
        print(i)