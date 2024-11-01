class Node:
    def __init__(self, label):
        self.label = label

    def __str__(self):
        return str(self.label)

class Graph:
    def __init__(self):
        self.nodes = {}
        self.adjancy_list = {}

    def add_node(self, label):
        node = Node(label)
        self.nodes[label] = node
        self.adjancy_list[node] = set()

    def add_edge(self, first, second):

        first_node = self.nodes.get(first)
        second_node = self.nodes.get(second)

        self.adjancy_list.get(first_node).add(second_node)
        self.adjancy_list.get(second_node).add(first_node)

        return True

    def bfs(self, source):
        root = self.nodes.get(source)
        q = [root]
        visited = set()

        while q:
            u = q.pop(0)
            if u in visited:
                continue
            # print(u)
            visited.add(u)
            print(len(self.adjancy_list.get(u)))
            for node in self.adjancy_list.get(u):
                if not node in visited:
                    q.append(node)

    def is_valid_node(self, label):

        if label in self.nodes:
            return True

        return False




graph = Graph()

edges = [[1, 2], [2, 3], [4, 2], [5, 2], [6, 2]]
nodes = set()

for edge in edges:
    nodes.add(edge[0])
    nodes.add(edge[1])


for node in nodes:
    graph.add_node(node)

for edge in edges:
    graph.add_edge(edge[0], edge[1])


graph.bfs(6)

