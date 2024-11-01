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
def kth_element(root):
    if root is None:
        return

    kth_element(root.left)
    data.append(root.val)
    kth_element(root.right)


def min_diff(root):
    if root is None:
        return 0

    if root.left:
        left_value = abs(root.val - root.left.val)
        

kth_element(node)

print(data[k-1])