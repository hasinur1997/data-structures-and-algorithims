from collections import defaultdict

graph = defaultdict(set)

edges = [[0, 3], [0, 1], [3, 2], [2, 4], [1, 2]]


for edge in edges:
    u, v = edge

    graph[u].add(v)
    graph[v].add(u)


def dfs(graph, source):
    visited = []
    stack = [source]
    while stack:
        node = stack.pop()

        if not node in visited:
            print(node)
            visited.append(node)
            for neighbour in graph[node]:
                if not neighbour in visited:
                    stack.append(neighbour)




def f(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return f(n-1) + f(n-2)


def fib(n):
    table = [None] * (n + 1)
    table[0] = 0
    table[1] = 1

    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]

    print(table)
    return table[n]

print(fib(20))


