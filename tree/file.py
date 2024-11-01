class TreeNode:
    def __init__(self, name):
        self.name = name
        self.is_file = False
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def delete_child(self, index):
        if index >= len(self.children):
            return

        self.children.pop(index)


class Tree:
    def __init__(self):
        pass
