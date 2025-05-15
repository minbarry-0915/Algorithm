# import sys
from collections import defaultdict

# sys.stdin = open('input.txt', 'r', encoding='utf-8')


def find_parent(node):
    path = []
    while node in parent:
        path.append(node)
        node = parent[node]
    path.append(node)
    return path


def get_subtree_size(node):
    count = 1
    for child in tree.get(node, []):
        count += get_subtree_size(child)
    return count


T = int(input())
for t in range(1, T + 1):
    v, e, n1, n2 = map(int, input().split())
    data = list(map(int, input().split()))
    tree = defaultdict(list) # {i: []}
    parent = defaultdict(int) # {i: number}

    for i in range(0, len(data), 2):
        p, c = data[i], data[i + 1]
        tree[p].append(c)
        parent[c] = p

    path1 = find_parent(n1)
    path2 = find_parent(n2)

    for ancestor in path1:
        if ancestor in path2:
            lca = ancestor
            break

    size = get_subtree_size(lca)
    print(f'#{t} {lca} {size}')