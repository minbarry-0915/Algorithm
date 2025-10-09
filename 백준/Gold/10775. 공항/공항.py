g = int(input())
p = int(input())
planes = list(int(input()) for _ in range(p))
parent = [i for i in range(g + 1)]
# 유니온 파인드
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a,b = find(a),find(b)
    parent[a] = b

# 주어진 범위에서 가장 큰 인덱스에 배치
count = 0
for gi in planes:
    root = find(gi)

    # 비행기가 어느 게이트에도 도킹할 수 없다면 break
    if root == 0:
        break

    union(root, root - 1) # 해당 인덱스를 찾으려하면, 한칸 작은곳으로 안내하자
    count += 1

print(count)