A, B = map(str, input().split())

A = A[::-1]
B = B[::-1]

result = max(int(A), int(B))
print(result)