def find_common_ancestor(parents, a, b):
    ancestors = set()

    while a:
        ancestors.add(a)
        a = parents[a]
    while b:
        if b in ancestors:
            return b
        b = parents[b]
    return None

def count_subtree(tree,root):
    count = 1
    for child in tree[root]:
        count += count_subtree(tree, child)
    return count

T = int(input())

for t in range(1, T + 1):
    v, e, num1, num2 = map(int, input().split())
    temp = list(map(int,input().split()))
    tree = {i: [] for i in range(1, v + 1)}
    parents = [0] * (v + 1)

    for i in range(0, len(temp), 2):
        parent, child = temp[i], temp[i + 1]
        tree[parent].append(child)
        parents[child] = parent

    lca = find_common_ancestor(parents, num1, num2)
    subtree_size = count_subtree(tree, lca)
    print(f'#{t} {lca} {subtree_size}')