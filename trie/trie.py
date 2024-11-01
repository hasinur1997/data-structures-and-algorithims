class Node:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.is_end = False

    def __str__(self):
        return self.val

    def add_child(self, key):
        self.children[key] = Node(key)

    def get_child(self, key):
        return self.children.get(key)

    def has_child(self, key):
        return self.children.get(key) is not None


class Trie:
    def __init__(self):
        self.root = Node(' ')

    def insert(self, word):
        current = self.root

        for ch in word:
            if not current.has_child(ch):
                current.add_child(ch)
            current = current.get_child(ch)

        current.is_end = True

    def contains(self, word):
        current = self.root

        for ch in word:
            if not current.has_child(ch):
                return False
            current = current.get_child(ch)

        return current.is_end


trie = Trie()


trie.insert('Cat')
trie.insert('Dog')
trie.insert('Fog')
trie.insert('Mog')

print(trie.contains('cat'))
