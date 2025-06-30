

def hanoi(n, start, end, via):
    if n == 1:
        print(start, end)
        return
    hanoi(n - 1, start, via, end)  # 제일 큰거 제외 나머지 중간으로 옮기기
    print(start, end)  # 제일 큰거 3번으로
    hanoi(n - 1, via, end, start)  # 중간으로 옮긴 나머지를 3번으로


n = int(input())
print(2 ** n - 1)
hanoi(n, 1, 3, 2)
