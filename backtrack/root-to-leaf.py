class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(5)
node4 = TreeNode(3)

node1.left = node2
node1.right = node4
node2.left = node3

def get_node(root, nodes=[]):
    if root is None:
        return nodes

    nodes.append(root.val)

    if root.left:
        nodes.append(get_node(root.left, nodes))

    if root.right:
        nodes.append(get_node(root.right, nodes))

    return


print(get_node(node1))

