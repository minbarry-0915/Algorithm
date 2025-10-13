n, k = map(int,input().split())
s = list(map(int,input().split()))

odd = 0
even = 0

end = 0
res = 0

for start in range(n):
    while odd <= k and end < n:
        if s[end] % 2 == 1:
            odd += 1
        else:
            even += 1
        end += 1
    res = max(res, even)
    if s[start] % 2 == 1:
        odd -= 1
    else:
        even -= 1
print(res)