class Node:
    def __init__(self, val=None):
        self.val = None
        self.children = {}
        self.end_word = False


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        current = self.root

        for ch in word:
            if current.children.get(ch) is None:
                current.children[ch] = Node(ch)
            current = current.children.get(ch)
        current.end_word = True

    def search(self, word: str) -> bool:
        current = self.root
        word = word.replace('.', '')
        for ch in word:
            if ch not in current.children:
                return False
            current = current.children[ch]

        return True


wordDictionary = WordDictionary()
wordDictionary.addWord("bad")
wordDictionary.addWord("dad")
wordDictionary.addWord("mad")
print(wordDictionary.search("pad"))
print(wordDictionary.search("bad"))
print(wordDictionary.search(".ad"))
print(wordDictionary.search("b.."))


test = '.ad'

test = test.replace('.', '')
print(len(test))