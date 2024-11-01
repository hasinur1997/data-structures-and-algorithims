class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []

        self.graph[u].append(v)

    def bfs(self, s):
        visited = []
        q = []

        q.append(s)
        visited = [s]

        while q:
            s = q.pop(0)
            print(s, end=" ")

            if s in self.graph:
                for i in self.graph[s]:
                    if i not in visited:
                        q.append(i)
                        visited.append(i)


if __name__ == '__main__':
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    g.add_edge(3, 5)

    g.bfs(0)