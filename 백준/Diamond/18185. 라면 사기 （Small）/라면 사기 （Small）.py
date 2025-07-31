n = int(input())
A = list(map(int,input().split()))

answer = 0

for i in range(n - 2):
    if A[i + 1] > A[i + 2]:
        # i+2번 공장과 짝지어서 3개 묶음을 만들 수 없는 초과 수량을
        # i번 공장과 먼저 2개 묶음으로 소진하자!
        count = min(A[i], A[i + 1] - A[i + 2])
        A[i] -= count
        A[i + 1] -= count
        answer += 5 * count

    # 3개 묶음 먼저
    count = min(A[i], A[i + 1], A[i + 2])
    A[i] -= count
    A[i + 1] -= count
    A[i + 2] -= count
    answer += 7 * count

for i in range(n - 1):
    count = min(A[i], A[i + 1])
    A[i] -= count
    A[i + 1] -= count
    answer += 5 * count

for i in range(n):
    answer += 3 * A[i]

print(answer)