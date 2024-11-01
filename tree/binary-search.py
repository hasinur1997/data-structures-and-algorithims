class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return self.val


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, item):
        self.root = self._insert(self.root, item)

    def _insert(self, node, val):
        if node is None:
            return Node(val)

        if val < node.val:
            node.left = self._insert(node.left, val)
        else:
            node.right = self._insert(node.right, val)

        return node

    def preorder(self):
        self._preorder(self.root)

    def _preorder(self, node):

        if node is None:
            return

        print(node.val)

        self._preorder(node.left)
        self._preorder(node.right)

    def bfs(self):
        queue = [self.root]
        data = []

        while queue:
            level_data = []

            for _ in range(len(queue)):
                node = queue.pop(0)
                level_data.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            data.append(level_data)

        return data[len(data) - 1]




def is_binary_search(root):
    if root is None:
        return True

    if root.left and root.val > root.left.val and root.right and root.val < root.right.val and is_binary_search(root.left) and is_binary_search(root.right):
        return True

    return False






tree = Tree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(4)
tree.insert(6)
tree.insert(11)
tree.insert(16)

tr = Tree()
tr.insert(10)
tr.insert(5)
tr.insert(15)
tr.insert(4)
tr.insert(6)
tr.insert(11)
tr.insert(16)

print(is_binary_search(tr.root))






# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# def levelOrder(root):
#     if not root:
#         return []
#
#     result = []
#     queue = [root]
#
#     while queue:
#         level_data = []
#
#         for _ in range(len(queue)):
#             node = queue.pop(0)
#             level_data.append(node.val)
#
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#
#         result.append(level_data)
#
#     return result
#
#
# # Example usage
# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)
#
# tree_levels = levelOrder(root)
# print(tree_levels)
