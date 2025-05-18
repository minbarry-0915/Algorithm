# 피사노 주기
# 주기의 길이가 P 일 때, N번째 피보나치 수를 M으로 나눈 나머지는 N%P번째 피보나치 수를 M을 나눈 나머지와 같습니다

n = int(input())
mod = 1000000
p = 1500000  # Pisano period for mod 1,000,000

n %= p # 한주기만 보면됨

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a + b) % mod
    return a

print(fib(n))

# def get_pisano_period(m):
#     a, b = 0, 1
#     for i in range(1, m * 6 + 1):  # upper bound of Pisano period is 6 * m
#         a, b = b, (a + b) % m
#         if a == 0 and b == 1:
#             return i
#
# print(get_pisano_period(1000000))  # 출력: 1500000