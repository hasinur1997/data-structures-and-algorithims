class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._find_words_with_prefix(node, prefix)

    def substring_exists(self, substring):
        node = self.root
        for char in substring:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def _find_words_with_prefix(self, node, current_prefix):
        suggestions = []
        if node.is_end_of_word:
            suggestions.append(current_prefix)

        for char, child in node.children.items():
            suggestions.extend(self._find_words_with_prefix(child, current_prefix + char))

        return suggestions

# Example usage
trie = Trie()
words = ["apple", "appetizer", "banana", "bat", "ball"]
for word in words:
    trie.insert(word)

substring = "at"
found = False

for word in words:
    if trie.substring_exists(word, substring):
        found = True
        break

if found:
    print(f'"{substring}" exists in the Trie')
else:
    print(f'"{substring}" does not exist in the Trie')

