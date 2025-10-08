n = int(input())
arr = [int(input()) for _ in range(n)]

# 양수일때 큰수끼리 곱해야 이득
# 1일때 무조건 더해야 이득
# 0일때 음수와 곱해서 없애는 용도
# 음수 같은 음수, 절댓값 큰수끼리 곱해야 이득

positives = []
negatives = []
ones = 0
zero =0
total = 0

for num in arr:
    if num > 1:
        positives.append(num)
    elif num == 1:
        ones += 1
    elif num == 0:
        zero += 1
    else:
        negatives.append(num)

positives.sort(reverse=True)
for i in range(0, len(positives), 2):
    if i + 1 < len(positives):
        total += positives[i] * positives[i + 1]
    else:
        total += positives[i]

negatives.sort()
for i in range(0, len(negatives), 2):
    if i + 1 < len(negatives):
        total += negatives[i] * negatives[i + 1]
    else:
        # 0이 있으면 없앨수 있음, 없으면 그냥 더해야됨
        if zero == 0:
            total += negatives[i]

total += ones
print(total)
