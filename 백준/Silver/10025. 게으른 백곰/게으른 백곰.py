n, k = map(int, input().split())

MAX_POS = 1000001
x = [0] * MAX_POS

for _ in range(n):
    g, i = map(int, input().split())
    x[i] += g  # 같은 위치에 여러 개 있을 수 있음

# 초기 윈도우 합 구하기
window_size = 2 * k + 1
current_sum = sum(x[:window_size])
max_ice = current_sum

# 슬라이딩 윈도우
for i in range(window_size, MAX_POS):
    current_sum = current_sum - x[i - window_size] + x[i]
    max_ice = max(max_ice, current_sum)

print(max_ice)
