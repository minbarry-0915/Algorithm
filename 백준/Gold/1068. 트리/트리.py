import sys
sys.setrecursionlimit(10 ** 6)
n = int(input())
parents = list(map(int, input().split()))
delete_node = int(input())

tree = {i: [] for i in range(n)}
root = -1

for child, parent in enumerate(parents):
    if parent == -1:
        root = child
    else:
        tree[parent].append(child)

def count_leaves(node):
    if node == delete_node:
        return 0
    if not tree[node]: # child가 없으면 본인이 leaf
        return 1

    total = 0
    for child in tree[node]:
        total += count_leaves(child)

    if total == 0: # 자식이 있는데 지워야 될 노드여서 다 지워짐
        return 1
    return total

if root == delete_node:
    print(0)
else:
    print(count_leaves(root))

