def inorder(current):
    if current > n :
        return
    inorder(current * 2)
    print(tree[current], end='')
    inorder(current * 2 + 1)
for t in range(1,11):
    n = int(input())
    tree = [0] * (n + 1)
    for i in range(1, n + 1):
        arr = list(input().split())
        tree[i] = arr[1]
    print(f'#{t}', end=' ')
    inorder(1)
    print()