N, M = map(int, input().split())

A = []
B = []
for _ in range(N):
    row = list(map(int,input().split()))
    A.append(row)

for _ in range(N):
    row = list(map(int,input().split()))
    B.append(row)

result = []
for i in range(N):
    row = []
    for j in range(M):
        row.append(A[i][j] + B[i][j])
    result.append(row)

for i in range(N):
    print(' '.join(map(str,result[i])))
