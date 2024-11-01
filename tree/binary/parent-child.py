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


tree = Tree()
nodes = [6, 7, 8, 2, 7, 1, 3, 9, 1, 4, 5]

for node in nodes:
    tree.insert(node)


def bfs(root_node):
    qeueue = [root_node]
    summation = 0

    while qeueue:
        node = qeueue.pop(0)
        grand_parent = find_grand_parent(root_node, node.val)

        if grand_parent and grand_parent.val % 2 == 0:
            summation += node.val

        if node.left:
            qeueue.append(node.left)
        if node.right:
            qeueue.append(node.right)

    return summation


def find_parent_node(root_node, child_value):
    # Base case: If the root is None or the root itself is the child node
    if root_node is None or root_node.val == child_value:
        return None

    # Check if the left child is the desired child node
    if root_node.left and root_node.left.val == child_value:
        return root_node

    # Check if the right child is the desired child node
    if root_node.right and root_node.right.val == child_value:
        return root_node

    # Recursively search in the left and right subtrees
    parent = find_parent_node(root_node.left, child_value)
    if parent:
        return parent

    parent = find_parent_node(root_node.right, child_value)
    if parent:
        return parent

    return None


def find_grand_parent(root_node, child_val):
    if root_node is None or root_node.val == child_val:
        return None

    if root_node.left and ((root_node.left.left and root_node.left.left.val == child_val) or (root_node.left.right and root_node.left.right.val == child_val)):
        return root_node

    if root_node.right and ((root_node.right.left and root_node.right.left.val == child_val) or (root_node.right.right and root_node.right.right.val == child_val)):
        return root_node

    grand_parent = find_grand_parent(root_node.left, child_val)

    if grand_parent:
        return grand_parent

    grand_parent = find_grand_parent(root_node.right, child_val)

    if grand_parent:
        return grand_parent

    return None




print(bfs(tree.root))



