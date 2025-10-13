T = int(input())
for _ in range(T):
    n,m,k = map(int,input().split())
    amounts = list(map(int,input().split()))

    total = sum(amounts[:m])
    case = 0
    if total < k:
        case += 1
    total -= amounts[0]
    total += amounts[(0 + m) % n]
    if n != m: # n 이랑 m이 같으면, 계속 같은 선택임
        for i in range(1, n):
            if total < k:
                case += 1

            total -= amounts[i]
            total += amounts[(i + m) % n]
    print(case)