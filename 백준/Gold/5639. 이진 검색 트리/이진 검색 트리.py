import sys

sys.setrecursionlimit(10**4)


preorder = []
for line in sys.stdin:
    line = line.strip()
    preorder.append(int(line))

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def insert(node,value):
    if value < node.value: # 왼쪽
        if node.left is None:
            node.left = Node(value)
        else:
            insert(node.left, value)
    else: #오른쪽
        if node.right is None:
            node.right = Node(value)
        else:
            insert(node.right, value)

root = Node(preorder[0])
for value in preorder[1:]:
    insert(root, value)

def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.value)

postorder(root)