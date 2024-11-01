class Node:
    def __init__(self, val=0):
        self.left = None
        self.right = None
        self.val = val

    def __str__(self):
        return self.val


def print_tree(root):
    if root is None:
        return
    print(root.val, end=' ')

    print_tree(root.left)
    print_tree(root.right)


def get_height(root):
    if root is None:
        return 0

    left = get_height(root.left)
    right = get_height(root.right)

    height = max(left, right)

    return height + 1


def count_leaf_node(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    left = count_leaf_node(root.left)
    right = count_leaf_node(root.right)

    return left + right


def count_node(root):
    if root is None:
        return 0

    left = count_node(root.left)
    right = count_node(root.right)

    return 1 + left + right


def add_odd(root):
    if root is None:
        return

    if root.val % 2 == 1:
        root.val = 0
    else:
        root.val = -1

    add_odd(root.left)
    add_odd(root.right)


node1 = Node(80)
node2 = Node(12)
node3 = Node(7)
node4 = Node(10)
node5 = Node(90)
node6 = Node(120)

root = node1

node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5

node3.left = node6

# print_tree(root)

print(count_node(root))

print_tree(root)
add_odd(root)
print_tree(root)


