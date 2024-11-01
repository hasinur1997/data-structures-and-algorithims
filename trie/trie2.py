class TrieNode:
    def __init__(self, val):
        self.val = val
        self.childs = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode(' ')

    def insert(self, word):
        currentNode = self.root

        for ch in word:
            if ch not in currentNode.childs:
                currentNode.childs[ch] = ch
            currentNode = TrieNode(ch)

        currentNode.is_end = True

    def search(self, word):
        currentNode = self.root

        for ch in word:
            if ch not in currentNode.childs:
                return False
            currentNode = TrieNode(ch)

        return currentNode.is_end