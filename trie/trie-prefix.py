class Node:
    def __init__(self, val = None):
        self.val = val
        self.children = {}
        self.endWord = False

class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word:
            if node.children.get(ch) is None:
                node.children[ch] = Node(ch)
            node = node.children.get(ch)

        node.endWord = True

    def search(self, word: str) -> bool:
        node = self.root

        for ch in word:
            if node.children.get(ch) is None:
                return False
            node = node.children.get(ch)

        return node.endWord

    def startsWith(self, prefix: str) -> bool:

        node = self.root

        for ch in prefix:
            if node.children.get(ch) is None:
                return False
            node = node.children.get(ch)

        return True

trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")

print(trie.search("app"))



# print('sef')