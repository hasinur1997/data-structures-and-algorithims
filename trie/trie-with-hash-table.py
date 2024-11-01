class Node:
    def __init__(self, val=None):
        self.val = val
        self.children = {}
        self.isWord = False

    def __str__(self):
        return self.val


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):

        current = self.root

        for ch in word:
            if current.children.get(ch) is None:
                current.children[ch] = Node(ch)
            current = current.children.get(ch)

        current.isWord = True

    def contains(self, word):

        if word is None:
            raise Exception('Argument must be word')
        current = self.root

        for ch in word:
            if current.children.get(ch) is None:
                return False

            current = current.children.get(ch)

        return current.isWord

    def search(self, prefix):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        return self._find_words(node, prefix)

    def _find_words(self, node, current_fix):
        suggestions = []

        if node.isWord:
            suggestions.append(current_fix)

        for char, child in node.children.items():
            suggestions.extend(self._find_words(child, current_fix + char))

        return suggestions

    def print(self):
        current = self.root


trie = Trie()
trie.insert('Cat')
trie.insert('Catter')
trie.insert('Crow')
results = trie.search('C')
