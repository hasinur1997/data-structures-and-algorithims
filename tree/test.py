class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, item):
        self.root = self._insert(self.root, item)

    def _insert(self, root, item):
        if root is None:
            return Node(item)

        if item < root.val:
            root.left = self._insert(root.left, item)
        else:
            root.right = self._insert(root.right, item)

        return root


def height(root):
    if root is None:
        return 0

    return 1 + max(height(root.left), height(root.right))


def diameter(root):
    if root is None:
        return 0

    lh = height(root.left)
    rh = height(root.right)

    ld = diameter(root.left)
    rd = diameter(root.right)

    return max(1+lh+rh, max(ld, rd))


def nodeatk(root, k):
    if root is None:
        return
    if k == 0:
        print(root.val)

    nodeatk(root.left, k - 1)
    nodeatk(root.right, k - 1)





