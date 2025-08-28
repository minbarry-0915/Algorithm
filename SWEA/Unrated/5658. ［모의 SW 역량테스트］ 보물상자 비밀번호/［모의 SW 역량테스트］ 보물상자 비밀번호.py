T = int(input())

for t in range(1, T + 1):
    n,k = map(int,input().split())
    s = input().strip()
    len_token = n // 4

    s2 = s + s
    cases = set()
    for shift in range(len_token): # 모든 경우 커버가능
        for start in range(shift, shift + n, len_token):
            token = s2[start: start + len_token]
            cases.add(int(token, 16))

    # 케이스 정렬
    cases_list = list(cases)
    cases_list.sort(reverse=True)
    print(f'#{t} {cases_list[k - 1]}')
