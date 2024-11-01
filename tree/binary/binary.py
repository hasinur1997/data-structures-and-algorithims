import sys

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, root, val):
        if root is None:
            return Node(val)

        left = self._count_node(root.left)
        right = self._count_node(root.right)

        if left <= right:
            root.left = self._insert(root.left, val)
        else:
            root.right = self._insert(root.right, val)

        return root

    def _count_node(self, root):
        if root is None:
            return 0
        return 1 + self._count_node(root.left) + self._count_node(root.right)

    def find_max(self):
        return self._find_max(self.root)

    def _find_max(self, root):
        if root is None:
            return -sys.maxsize - 1

        result = root.val
        left = self._find_max(root.left)
        right = self._find_max(root.right)

        if left > result:
            result = left

        if right > result:
            result = right

        return result

    def find_min(self):
        return self._find_min(self.root)

    def _find_min(self, root):
        if root is None:
            return sys.maxsize

        result = root.val
        left = self._find_min(root.left)
        right = self._find_min(root.right)

        if left < result:
            result = left

        if right < right:
            result = right

        return result

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, root, key):
        if root is None or root.val == key:
            return root

        if key < root.val:
            return self._search(root.left, key)
        else:
            return self._search(root.right, key)


tr = BinaryTree()
tr.insert(2)
tr.insert(10)
tr.insert(12)
tr.insert(4)
tr.insert(90)
tr.insert(120)
tr.insert(14)
tr.insert(50)
tr.insert(60)
tr.insert(1200)
tr.insert(12)
tr.insert(1267)
tr.insert(1)


print(tr.find_min())
