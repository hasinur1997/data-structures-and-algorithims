class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return f"Node {self.val}"


class Tree:

    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def height(self):
        return self._height(self.root)

    def min(self):
        return self._min(self.root)

    def max(self):
        return self._max(self.root)

    def contains(self, item):
        return self._contains(self.root, item)

    def count(self):
        return self._count(self.root)

    def count_leaves(self):
        return self._count_leavs(self.root)

    def are_siblings(self, item1, item2):
        return self._are_siblings(self.root, item1, item2)

    def get_ancestors(self, item):
        return self._get_ancestors(self.root, item)

    def _insert(self, root, val):
        if root is None:
            return Node(val)

        if val < root.val:
            root.left = self._insert(root.left, val)

        else:
            root.right = self._insert(root.right, val)

        return root

    def _height(self, root):

        if root is None:
            return 0

        left = self._height(root.left)
        right = self._height(root.right)

        return 1 + max(left, right)

    def _min(self, root):
        if root is None:
            return float('inf')
        left = self._min(root.left)
        right = self._min(root.right)

        return min(root.val, left, right)

    def _max(self, root):
        if root is None:
            return float('-inf')
        left = self._max(root.left)
        right = self._max(root.right)

        return max(root.val, left, right)

    def _contains(self, root, item):
        if root is None:
            return False

        return root.val == item or self._contains(root.left, item) or self._contains(root.right, item)

    def _count(self, root):
        if root is None:
            return 0

        return 1 + self._count(root.left) + self._count(root.right)

    def _count_leavs(self, root):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        return self._count_leavs(root.left) + self._count_leavs(root.right)

    def _are_siblings(self, root, item1, item2):
        if root is None:
            return False

        if root.left and root.right:
            left = root.left.val
            right = root.right.val

            if left == item1 and right == item2:
                return True

            if left == item2 and right == item1:
                return True

        return self._are_siblings(root.left, item1, item2) or self._are_siblings(root.right, item1, item2)

    def _get_ancestors(self, root, target):

        if root is None:
            return []

        if root.val == target:
            return []

        left_ancestors = self._get_ancestors(root.left, target)

        if left_ancestors is not None:
            left_ancestors.append(root.val)

            return left_ancestors

        right_ancestors = self._get_ancestors(root.right, target)

        if right_ancestors is not None:
            right_ancestors.append(root.val)

            return right_ancestors

        return []



tree = Tree()

tree.insert(10)
tree.insert(5)
tree.insert(11)
tree.insert(4)
tree.insert(6)
tree.insert(12)
tree.insert(9)
tree.insert(0)
tree.insert(120)


print(tree.get_ancestors(89))
