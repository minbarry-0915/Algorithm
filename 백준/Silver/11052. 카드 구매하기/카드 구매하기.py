
import sys
input = sys.stdin.readline

n = int(input())  # 카드 개수
cards = list(map(int, input().split()))  # 카드팩 가격
dp = [0] * (n + 1)  # dp[i]: i개의 카드를 구매하는 최대 비용

for i in range(1, n + 1):  # i개의 카드를 구매하는 경우
    for j in range(1, i + 1):  # j개의 카드가 포함된 카드팩 사용
        dp[i] = max(dp[i], dp[i - j] + cards[j - 1])

print(dp[n])  # n개의 카드를 구매하는 최대 비용 출력
