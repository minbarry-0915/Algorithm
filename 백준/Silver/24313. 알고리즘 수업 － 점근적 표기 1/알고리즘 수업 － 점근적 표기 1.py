a1, a0 = map(int, input().split())  # f(n) = a1 * n + a0
c = int(input())  # c
n0 = int(input())  # n0

# O(n) 정의를 만족하는지 확인
for n in range(n0, 101):  # n0부터 100까지 반복
    f_n = a1 * n + a0
    c_times_n = c * n
    if f_n > c_times_n:
        print(0)  # 만족하지 않으면 0 출력
        break
else:
    print(1)  # 모든 n에 대해 만족하면 1 출력