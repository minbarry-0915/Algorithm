n,k = map(int,input().split())
dolls = list(map(int,input().split()))

start = 0
end = 0
min_len = int(1e9)
cnt = 0

while True:
    if cnt >= k:
        min_len = min(min_len, end - start)
        if dolls[start] == 1:
            cnt -= 1
        start += 1
    elif end == n:
        break
    else:
        if dolls[end] == 1:
            cnt += 1
        end += 1

print(min_len if min_len != int(1e9) else -1)
