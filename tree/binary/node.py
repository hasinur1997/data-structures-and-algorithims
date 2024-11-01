class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value =

        class Node:
            def __init__(self, val):
                self.left = None
                self.right = None
                self.val = val

        class Tree:
            def __init__(self):
                self.root = None

            def insert(self, item):
                pass

            def _insert(self, root, item):
                node = Node(item)

                if root is None:
                    return node

                if root.left is None:
                    root.left = node
                else:
                    root.right = node

                return node
