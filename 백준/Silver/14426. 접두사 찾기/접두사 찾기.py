import sys
input = sys.stdin.readline

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False # 단어의 끝

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children: #노드에 자식중에 없으면
                node.children[char] = TrieNode() #노드 생성
            node = node.children[char] #있으면 이동
        node.is_end = True
    
    def starts_with(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
n, m = map(int, input().split())
trie = Trie()
for _ in range(n):
    trie.insert(input().strip())

count = 0
for _ in range(m):
    prefix = input().strip()
    if trie.starts_with(prefix):
        count += 1

print(count)
