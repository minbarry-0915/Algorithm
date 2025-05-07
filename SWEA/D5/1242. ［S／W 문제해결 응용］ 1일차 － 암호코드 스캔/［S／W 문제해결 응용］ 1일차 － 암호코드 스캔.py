# 앞의 0의 비율을 제외한 나머지 숫자 비율(101)
code_dict = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9,
}
T = int(input())
for t in range(1, T + 1):
    n, m = map(int, input().split())
    hexadecimals = list(set([input().rstrip() for _ in range(n)]))  # 배열이 다른 줄만 남게됨
    storage = []
    answer = 0
    for i in hexadecimals:
        binaries = format(int(i, 16), 'b').lstrip('0')  # 왼쪽 0 삭제 : 가변 길이임, 어차피 1 비율부터 검사할거임
        # 비율 계산
        n1 = n2 = n3 = 0
        cnt = 0
        temp = []
        for token in binaries:
            if token == '1' and n2 == 0:  # 1이 나왔는데 n2를 안셋으면 n1구간임
                n1 += 1
            elif token == '0' and n1 != 0 and n3 == 0:  # 0이 나왔는데 n1을 셋고 n3를 안셋으면 => n2 구간
                n2 += 1
            elif token == '1' and n2 != 0:
                n3 += 1
            elif n3 != 0:  # n3가 0이 아니면 -> 이진수 코드 한블럭 끝
                cnt += 1
                r = min(n1, n2, n3)
                nums = code_dict[(n1 // r, n2 // r, n3 // r)]
                temp.append(str(nums))
                n1 = n2 = n3 = 0  # 비율 초기화
                if cnt == 8:  # 암호 완성
                    odd = temp[::2]
                    even = temp[1::2]
                    if (sum(map(int, odd)) * 3 + sum(map(int, even))) % 10 == 0:
                        if temp not in storage:
                            storage.append(temp)
                            answer += sum(map(int, temp))
                    cnt = 0
                    temp = []
    print(f'#{t} {answer}')
