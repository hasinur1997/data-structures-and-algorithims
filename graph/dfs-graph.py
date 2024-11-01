class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []

        self.graph[u].append(v)

    def dfs(self, v):
        visited = set()
        self._dfs(v, visited)

    def _dfs(self, v, visited):
        visited.add(v)
        print(v, end=' ')

        if v in self.graph:
            for i in self.graph[v]:
                if i not in visited:
                    self._dfs(i, visited)


if __name__ == '__main__':
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    g.dfs(2)
