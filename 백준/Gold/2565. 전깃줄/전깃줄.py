

# 접근: a의 번호가 작은 순서대로 정렬을 하고
# 앞순서의 b가 뒷순서의 b보다 작은 경우가 최대로 이어지는 경우
n = int(input())
lines = [tuple(map(int,input().split())) for _ in range(n)]

lines.sort()

b = [line[1] for line in lines]

dp = [1] * n # 장애물없이 최대로 연결되는 전깃줄의 수
for i in range(n):
    for j in range(i):
        if b[j] < b[i]: # 현재의 전깃줄번호가 이전것들보다 항상 커야됨 -> 안 크면 제거대상
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
