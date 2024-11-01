class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root

        for ch in word:
            ch = ch.lower()
            index = ord(ch) - ord('a')

            if current.children[index] is None:
                node = TrieNode()
                current.children[index] = node
                current = node
            else:
                current = current.children[index]

        current.isWord = True



trie = Trie()
trie.insert('Cat')
trie.insert('dog')
trie.insert('Cab')

print(trie.root.children[2])

