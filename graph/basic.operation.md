# Graph Operations Documentation

## Table of Contents
1. [Adding and Removing Vertices and Edges](#adding-and-removing-vertices-and-edges)
2. [Checking Connectivity (Reachability)](#checking-connectivity-reachability)
3. [Path Finding](#path-finding)
4. [Cycle Detection](#cycle-detection)
5. [Topological Sorting](#topological-sorting)
6. [Finding Strongly Connected Components (SCC)](#finding-strongly-connected-components-scc)
7. [Finding Minimum Spanning Tree (MST)](#finding-minimum-spanning-tree-mst)
8. [Counting Components](#counting-components)
9. [Graph Coloring](#graph-coloring)
10. [Maximum Flow](#maximum-flow)
11. [Basic Operations Code Example](#basic-operations-code-example)

---

### 1. Adding and Removing Vertices and Edges

- **Add Vertex**: Add a new node to the graph.
- **Remove Vertex**: Deletes a node and all edges connected to it.
- **Add Edge**: Creates a connection between two vertices.
- **Remove Edge**: Deletes a connection between two vertices.

#### Example (Adjacency List Representation)
```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
```

---

### 2. Checking Connectivity (Reachability)
Determines if there is a path between two vertices. Common methods:
- **Breadth-First Search (BFS)**: Good for finding shortest paths in unweighted graphs.
- **Depth-First Search (DFS)**: Used to explore all reachable nodes from a given starting point.

---

### 3. Path Finding
Finds paths between vertices:
- **Simple Path**: Each vertex appears at most once.
- **Shortest Path**: Path with the minimum edges (unweighted) or minimum weight (weighted).

#### Common Algorithms
- **BFS**: Finds shortest paths in unweighted graphs.
- **Dijkstra’s Algorithm**: Finds shortest paths in weighted graphs (non-negative weights).
- **Bellman-Ford**: Works with negative weights.

---

### 4. Cycle Detection
Checks if a graph contains any cycles.
- **Undirected Graphs**: DFS with visited checks.
- **Directed Graphs**: DFS with back edges or **Kahn’s Algorithm**.

---

### 5. Topological Sorting
Orders vertices in a **Directed Acyclic Graph (DAG)** so that for every directed edge `U → V`, `U` comes before `V`.
- **Kahn’s Algorithm** (BFS-based)
- **DFS-based Topological Sort**

---

### 6. Finding Strongly Connected Components (SCC)
Identifies **subgraphs** in a directed graph where every vertex is reachable from every other vertex within the subgraph.

#### Algorithms
- **Kosaraju’s Algorithm**
- **Tarjan’s Algorithm**

---

### 7. Finding Minimum Spanning Tree (MST)
Finds the subset of edges that connect all vertices with minimum total weight (in weighted graphs).

#### Common Algorithms
- **Kruskal’s Algorithm**: Uses sorting and union-find.
- **Prim’s Algorithm**: Uses priority queues.

---

### 8. Counting Components
Counts the number of **connected components** in an undirected graph, where each component is a maximal set of connected vertices.

---

### 9. Graph Coloring
Assigns colors to vertices so that no two adjacent vertices share the same color. Useful for:
- **Map Coloring**: Regions must have different colors if they share a border.
- **Scheduling**: Assigning time slots or resources without conflicts.

---

### 10. Maximum Flow
Finds the maximum possible flow from a source to a sink in a flow network.

#### Common Algorithms
- **Ford-Fulkerson Method**: Basic approach.
- **Edmonds-Karp**: BFS-based max-flow calculation.

---

### 11. Basic Operations Code Example

Here is a sample Python class for a graph using an adjacency list, with methods to add/remove vertices and edges.

```python
class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        # Add an undirected edge between vertex1 and vertex2
        if vertex1 in self.graph:
            self.graph[vertex1].append(vertex2)
        if vertex2 in self.graph:
            self.graph[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph[vertex1]:
            self.graph[vertex1].remove(vertex2)
        if vertex2 in self.graph and vertex1 in self.graph[vertex2]:
            self.graph[vertex2].remove(vertex1)

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            for neighbor in self.graph[vertex]:
                self.graph[neighbor].remove(vertex)
            del self.graph[vertex]

    def display(self):
        for vertex in self.graph:
            print(f"{vertex} --> {self.graph[vertex]}")
```

#### Usage

```python
# Creating the graph and adding vertices
g = Graph()
g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')

# Adding edges
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')

# Display graph
g.display()

# Removing an edge and a vertex
g.remove_edge('A', 'B')
g.remove_vertex('D')

# Display modified graph
g.display()
```

---