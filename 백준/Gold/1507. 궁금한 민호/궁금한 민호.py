import sys
# sys.stdin = open('input.txt','r')

n = int(input())
adj = [list(map(int,input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j or j == k or i == k:
                continue
            if adj[i][j] > adj[i][k] + adj[k][j]:
                print(-1)
                exit()

# 불필요한 간선 제거
result = 0
for i in range(n):
    for j in range(i+1, n):  # 무방향 그래프이므로 중복 방지
        necessary = True
        for k in range(n):
            # 직접가나 거쳐서 가나 똑같으므로 직접가는 간선은 필요하지 않음
            if k != i and k != j and adj[i][j] == adj[i][k] + adj[k][j]:
                necessary = False
                break
        if necessary:
            result += adj[i][j]

print(result)