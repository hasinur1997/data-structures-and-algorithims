class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []

        self.graph[u].append(v)

    def dfs(self, s):
        visited = []
        stack = []

        stack.append(s)
        results = []
        while stack:
            s = stack[-1]
            stack.pop()
            if s not in visited:
                # print(s, end=' ')
                results.append(s)
                visited.append(s)

            if s not in self.graph:
                continue
            for i in self.graph[s]:
                if i not in visited:
                    stack.append(i)

        return results


if __name__ == '__main__':
    g = Graph()
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(1, 4)

    dt = g.dfs(0)

    print(dt)
