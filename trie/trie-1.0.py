class Node:
    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.endWord = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        current = self.root

        for ch in word:
            ch = ch.lower()
            if current.children.get(ch) is None:
                current.children[ch] = Node(ch)

            current = current.children.get(ch)

        current.endWord = True

    def contains(self, word):
        node = self.root
        word = word.lower()
        for ch in word:
            if node.children.get(ch) is None:
                return False

            node = node.children.get(ch)

        return node.endWord

    def search(self, prefix):
        prefix = prefix.lower()
        if not prefix:
            return []
        node = self.root

        for ch in prefix:
            if node.children.get(ch) is None:
                return []

            node = node.children.get(ch)

        return self._find_word(node, prefix)

    def _find_word(self, node, prefix):
        suggessions = []

        if node.endWord:
            suggessions.append(prefix)

        for char, child in node.children.items():
            suggessions.extend(self._find_word(child, prefix + char))

        return suggessions




trie = Trie()
trie.insert('Apple')
trie.insert('Mango')
trie.insert('Pakistan')
trie.insert('Papper')
trie.insert('Water')
trie.insert('Guava')
trie.insert('Parbol')

print(trie.contains('34ater'))