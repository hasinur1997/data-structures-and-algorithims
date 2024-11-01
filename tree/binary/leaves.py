class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self._insert(self.root, val)

    def _insert(self, root, val):

        if root is None:
            return Node(val)

        if val < root.val:
            root.left = self._insert(root.left, val)
        else:
            root.right = self._insert(root.right, val)

        return root

    def print_leaf(self):
        self._print_leaf(self.root)

    def _print_leaf(self, root):
        if root is None:
            return

        if root.left is None and root.right is None:
            print(root.val)

        self._print_leaf(root.left)
        self._print_leaf(root.right)


tree = Tree()
tree.insert(30)
tree.insert(26)
tree.insert(32)
tree.insert(22)
tree.insert(35)
tree.insert(29)

tree2 = Tree()
tree2.insert(30)
tree2.insert(26)
tree2.insert(32)
tree2.insert(21)
tree2.insert(35)
tree2.insert(29)


def is_right_sequense(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    if is_leaf(root1) and is_leaf(root2) and root1.val == root2.val:
        return True

    return is_right_sequense(root1.left, root2.left) and is_right_sequense(root1.right, root2.right)


def is_leaf(node):
    if node is Node:
        return False

    if node.left is None and node.right is None:
        return True

    return False


print(is_right_sequense(tree.root, tree2.root))
