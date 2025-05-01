from collections import deque


for _ in range(10):
    t = int(input())
    num_lst = deque(map(int, input().split()))

    while True:
        for i in range(1, 6):  # 1~5 순차적으로 감소
            num = num_lst.popleft()
            num -= i
            if num <= 0:
                num = 0
                num_lst.append(num)
                break  # 한 사이클 중 num이 0이 되었으면 종료
            num_lst.append(num)
        if num == 0:
            break

    print(f'#{t}', *num_lst)