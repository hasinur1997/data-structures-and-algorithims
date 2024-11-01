class Node:
    def __init__(self, label):
        self.label = label

    def __str__(self):
        return self.label

class Graph:
    def __init__(self):
        self.nodes = {}
        self.adjancyList = {}

    def add_node(self, label):
        node = Node(label)
        self.nodes[label] = node
        self.adjancyList[node] = set()

    def remove_node(self, label):
        if not self.is_valid(label):
            return
        node = self.nodes.get(label)

        for n in self.adjancyList:
            items = self.adjancyList.get(n)

            if node in items:
                items.remove(node)

        self.nodes.pop(label)

    def add_edge(self, first, second):
        if not self.is_valid(first) and not self.is_valid(second): 
            return

        first = self.nodes.get(first)
        second = self.nodes.get(second)
            
        self.adjancyList.get(first).add(second)

    def get_edge(self, label):
        if not self.is_valid(label):
            return False
        node = self.nodes.get(label)

        return self.adjancyList.get(node)
    def remove_edge(self, first, second):
        if not self.is_valid(first):
            return
        
        if not self.is_valid(second):
            return
        first = self.nodes.get(first)
        second = self.nodes.get(second)

        self.adjancyList.get(first).remove(second)

    def dfs(self, root):
        node = self.nodes.get(root)

        self._dfs(node)

    def _dfs(self, root, visited = set()):
        print(root)
        visited.add(root)

        for node in self.adjancyList.get(root):
            if not node in visited:
                self._dfs(node, visited)

    def dfs_iterative(self, root):
        root = self.nodes.get(root)
        print(root)
        for node in self.adjancyList.get(root):
            print(node)

    def bfs(self, root):
        node = self.nodes.get(root)

        visited = set()
        queue = [node]

        while len(queue) != 0:
            current = queue.pop(0)

            if current in visited:
                continue
            
            print(current)
            visited.add(current)

            for neighbour in self.adjancyList.get(current):
                if not neighbour in visited:
                    queue.append(neighbour)

    def is_valid(self, node):
        if node in self.nodes:
            return True

        return False


graph = Graph()

graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')
graph.add_node('E')

graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('D', 'E')
graph.add_edge('A', 'D')
graph.add_edge('A', 'C')

# print(len(graph.get_edge('A')))

# graph.dfs('B')
graph.bfs('E')

