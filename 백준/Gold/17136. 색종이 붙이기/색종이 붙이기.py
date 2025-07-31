'''
붙일 가치가 있는 구역을 탐색해서 색종이를 계속 붙였다 떼는 백트랙킹 진행
'''
def can_attach(x,y,size):
    if x + size > n or y + size > n:
        return False
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != 1:
                return False
    return True

def attach(x,y,size,val):
   for i in range(x, x + size):
       for j in range(y, y + size):
           paper[i][j] = val

def simulation(count):
    global result
    # 종료 조건: 더 나은 답이 이미 존재
    if count >= result:
        return

    for i in range(10):
        for j in range(10):
            if paper[i][j] == 1:
                for size in reversed(range(1, 6)):
                    if confetti[size - 1] > 0 and can_attach(i, j, size):
                        attach(i, j, size, 0)
                        confetti[size - 1] -= 1
                        simulation(count + 1)
                        confetti[size - 1] += 1
                        attach(i, j, size, 1)
                return  # 반드시 return. (첫 번째 1만 처리해야 함)
    result = min(result, count)

n = 10
paper = [list(map(int,input().split())) for _ in range(n)]
confetti = [5,5,5,5,5]
result = int(1e9)
simulation(0)
print(result if result != int(1e9) else -1)