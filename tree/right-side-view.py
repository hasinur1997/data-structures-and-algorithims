class TreeNode:
    def __init__(self, val=0):
        self.left = None
        self.right = None
        self.val = val


node = TreeNode(3)
node1 = TreeNode(1)
node2 = TreeNode(4)
node3 = TreeNode(2)

node.left = node1
node.right = node2
node1.right = node3

data = []

k = 3


def right_side_view(root):
    if root is None:
        return

    data.append(root.val)
    right_side_view(root.right)


right_side_view(node)

print(data)



