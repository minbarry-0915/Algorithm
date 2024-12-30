T = int(input())  # 테스트 케이스 개수

for _ in range(T):
    H, W, N = map(int, input().split())  # H: 층 수, W: 방 수, N: N번째 손님

    # 층 배정은 N % H, 방 배정은 N // H + 1
    floor = N % H if N % H != 0 else H  # 층 번호는 1부터 H까지, N이 H로 나누어 떨어지면 H층
    room = (N - 1) // H + 1  # 방 번호는 1번부터 시작

    print(f"{floor}{room:02d}")  # 방 번호 출력