S = int(input())

result = 0
cnt = 0

while True:
    cnt += 1
    result += cnt

    if result > S:
        break

print(cnt - 1)