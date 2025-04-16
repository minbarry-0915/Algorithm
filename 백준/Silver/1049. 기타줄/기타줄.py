import math
n, m = map(int, input().split())

min_package = int(1e9)
min_single = int(1e9)

for _ in range(m):
    package, single = map(int, input().split())
    min_package = min(min_package, package)
    min_single = min(min_single, single)

# 다 패키지로 샀을때
all_package = math.ceil(n / 6) * min_package
# 다 싱글로 샀을떄
all_single = n * min_single
# 몫만큼은 패키지로 사고 나머지는 싱글로
mix = (n // 6) * min_package + (n % 6) * min_single

print(min(all_package, all_single, mix))