# Graphs

Graphs are an essential data structure in computer science, representing a set of nodes (vertices) connected by edges. Graphs are versatile and are used to model relationships between objects, such as social networks, transportation systems, communication networks, and many other applications.


- [Graphs](#graphs)
    - [Key Concepts in Graphs](#key-concepts-in-graphs)
    - [Graph Representation](#graph-representation)
    - [Common Graph Algorithms](#common-graph-algorithms)
    - [1. Depth-First Search (DFS)](#1-depth-first-search-dfs)
    - [2. Breadth-First Search (BFS)](#2-breadth-first-search-bfs)
    - [3. Dijkstra’s Shortest Path Algorithm](#3-dijkstras-shortest-path-algorithm)
    - [4. Bellman-Ford Algorithm](#4-bellman-ford-algorithm)
    - [5. Floyd-Warshall Algorithm](#5-floyd-warshall-algorithm)
    - [6. Minimum Spanning Tree (MST)](#6-minimum-spanning-tree-mst)
      - [Prim’s Algorithm](#prims-algorithm)
      - [Kruskal’s Algorithm](#kruskals-algorithm)
    - [7. Topological Sorting](#7-topological-sorting)
      - [DFS-Based Approach:](#dfs-based-approach)
    - [Additional Notes:](#additional-notes)
  - [Summary](#summary)


### Key Concepts in Graphs

1. **Vertices (Nodes)**: The entities in a graph.
2. **Edges (Links)**: Connections between pairs of vertices.
3. **Directed vs. Undirected**:
   - **Directed Graph (Digraph)**: Each edge has a direction, going from one vertex to another.
   - **Undirected Graph**: Edges have no direction and connect two vertices bidirectionally.
4. **Weighted vs. Unweighted**:
   - **Weighted Graph**: Each edge has a weight or cost associated with it.
   - **Unweighted Graph**: All edges have equal weight.
5. **Connected vs. Disconnected**:
   - **Connected Graph**: There's a path between every pair of vertices.
   - **Disconnected Graph**: Some vertices cannot be reached from others.

### Graph Representation

Graphs can be represented in several ways, depending on the problem requirements and efficiency considerations:

1. **Adjacency Matrix**:
   - A 2D array where each cell `(i, j)` is `1` (or the weight of the edge) if there is an edge from vertex `i` to vertex `j`; otherwise, it’s `0`.
   - Efficient for dense graphs but requires O(V^2) space.

2. **Adjacency List**:
   - An array or list where each index represents a vertex, and each element at that index points to a list of neighbors (or edges).
   - Efficient for sparse graphs, with an average space complexity of O(V + E), where V is the number of vertices and E is the number of edges.

3. **Edge List**:
   - A list of all edges, where each edge is represented as a tuple (or triple if weighted), such as `(u, v)` or `(u, v, weight)`.

---

### Common Graph Algorithms

1. **Depth-First Search (DFS)**
2. **Breadth-First Search (BFS)**
3. **Dijkstra’s Shortest Path Algorithm**
4. **Bellman-Ford Algorithm**
5. **Floyd-Warshall Algorithm**
6. **Minimum Spanning Tree (MST) (Prim’s and Kruskal’s algorithms)**
7. **Topological Sorting**

Let’s explore these algorithms with explanations, examples, and code.

---

### 1. Depth-First Search (DFS)

**Description**: DFS explores as far as possible along each branch before backtracking. It’s commonly used for pathfinding, detecting cycles, and traversing all nodes.

**Implementation**:
- Use a stack (explicitly or implicitly with recursion) to explore nodes.

**Code Example** (Recursive):

```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)  # Process the node

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
```

**Time Complexity**: O(V + E), where V is the number of vertices and E is the number of edges.

---

### 2. Breadth-First Search (BFS)

**Description**: BFS explores all nodes at the current level before moving to the next level. It’s used for finding the shortest path in unweighted graphs and for level-order traversal.

**Implementation**:
- Use a queue to explore nodes level by level.

**Code Example**:

```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex)  # Process the node
            queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)
```

**Time Complexity**: O(V + E), where V is the number of vertices and E is the number of edges.

---

### 3. Dijkstra’s Shortest Path Algorithm

**Description**: Dijkstra’s algorithm finds the shortest path from a starting vertex to all other vertices in a weighted graph with non-negative weights.

**Implementation**:
- Use a priority queue (min-heap) to keep track of the minimum distance from the source to each node.

**Code Example**:

```python
import heapq

def dijkstra(graph, start):
    min_heap = [(0, start)]  # (distance, vertex)
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    while min_heap:
        current_distance, current_vertex = heapq.heappop(min_heap)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))

    return distances
```

**Time Complexity**: O((V + E) log V) with a binary heap.

---

### 4. Bellman-Ford Algorithm

**Description**: Bellman-Ford finds the shortest path from a single source to all other vertices, even in graphs with negative weights. It can also detect negative weight cycles.

**Implementation**:
- Relax all edges repeatedly for `V - 1` times, where V is the number of vertices.

**Code Example**:

```python
def bellman_ford(graph, V, start):
    distances = [float('inf')] * V
    distances[start] = 0

    for _ in range(V - 1):
        for u, v, weight in graph:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight

    # Detect negative weight cycles
    for u, v, weight in graph:
        if distances[u] + weight < distances[v]:
            print("Graph contains a negative weight cycle")
            return None

    return distances
```

**Time Complexity**: O(V * E), where V is the number of vertices and E is the number of edges.

---

### 5. Floyd-Warshall Algorithm

**Description**: Floyd-Warshall finds the shortest paths between all pairs of vertices in a weighted graph, handling negative weights but not negative cycles.

**Implementation**:
- Use dynamic programming to update distances between all pairs of vertices.

**Code Example**:

```python
def floyd_warshall(graph, V):
    dist = [[float('inf')] * V for _ in range(V)]
    for v in range(V):
        dist[v][v] = 0

    for u, v, weight in graph:
        dist[u][v] = weight

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist
```

**Time Complexity**: O(V^3), where V is the number of vertices.

---

### 6. Minimum Spanning Tree (MST)

An MST is a subset of edges in a connected, weighted graph that connects all vertices with the minimum possible total edge weight.

#### Prim’s Algorithm

**Description**: Prim’s algorithm builds an MST by adding edges with the smallest weight that connect a new vertex to the existing MST.

**Code Example**:

```python
import heapq

def prim_mst(graph, start):
    mst_cost = 0
    visited = set()
    min_heap = [(0, start)]

    while min_heap:
        weight, vertex = heapq.heappop(min_heap)
        if vertex in visited:
            continue
        mst_cost += weight
        visited.add(vertex)

        for neighbor, edge_weight in graph[vertex]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor))

    return mst_cost
```

**Time Complexity**: O(E log V), where E is the number of edges and V is the number of vertices.

---

#### Kruskal’s Algorithm

**Description**: Kruskal’s algorithm builds an MST by sorting edges by weight and adding edges to the MST if they don’t form a cycle (using union-find for cycle detection).

**Code Example**:

```python
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x

def kruskal_mst(edges, n):
    edges.sort(key=lambda x: x[2])  # Sort by weight
    ds = DisjointSet(n)
    mst_cost = 0
    mst_edges = []

    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):
            mst_cost += weight
            mst_edges.append((u, v, weight))
            ds.union(u, v)

    return mst_cost, mst_edges
```

**Time Complexity**: O(E log E), where E is the number of edges (due to sorting).

---

### 7. Topological Sorting

```markdown
**Description**: Topological sorting is a linear ordering of vertices in a directed acyclic graph (DAG), where for every directed edge `u -> v`, vertex `u` appears before vertex `v` in the ordering. It's commonly used in scheduling tasks, dependency resolution, and compiling order.

**Implementation**:
- Use **Kahn’s Algorithm** (BFS-based) or a DFS-based approach.

#### Kahn's Algorithm (BFS-based):
```python
from collections import deque, defaultdict

def topological_sort_kahn(vertices, edges):
    in_degree = {v: 0 for v in vertices}
    graph = defaultdict(list)
    
    # Build the graph and in-degree count
    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    # Collect nodes with no incoming edges
    zero_in_degree = deque([v for v in vertices if in_degree[v] == 0])
    topo_order = []

    while zero_in_degree:
        node = zero_in_degree.popleft()
        topo_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                zero_in_degree.append(neighbor)

    if len(topo_order) != len(vertices):
        raise ValueError("Graph has at least one cycle")
    
    return topo_order
```

#### DFS-Based Approach:
```python
def topological_sort_dfs(vertices, edges):
    visited = set()
    stack = []
    graph = defaultdict(list)
    
    # Build the graph
    for u, v in edges:
        graph[u].append(v)

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)
    
    for vertex in vertices:
        if vertex not in visited:
            dfs(vertex)

    return stack[::-1]  # Reverse the stack for topological order
```

**Time Complexity**:  
- Kahn's Algorithm: `O(V + E)`  
- DFS-Based: `O(V + E)`  

---

### Additional Notes:

- **Cycle Detection in Graphs**:
  - Use DFS with a "visited stack" to detect back edges (for directed graphs).
  - For undirected graphs, detect cycles by tracking visited nodes and parent references.
  
- **Applications of Graph Algorithms**:
  - Shortest Path: Navigation systems, networking.
  - Topological Sorting: Build systems, task scheduling.
  - Minimum Spanning Tree: Designing communication networks, reducing costs.


## Summary
Here’s a summary of the time complexities of the key graph algorithms presented, formatted as a table:

```markdown
| **Algorithm**                | **Time Complexity**          | **Space Complexity**       | **Description**                                                                 |
|-------------------------------|------------------------------|----------------------------|---------------------------------------------------------------------------------|
| **Depth-First Search (DFS)** | `O(V + E)`                  | `O(V)` (visited set)       | Traverses as far as possible down each branch before backtracking.              |
| **Breadth-First Search (BFS)**| `O(V + E)`                  | `O(V)` (queue)             | Explores all neighbors level by level.                                          |
| **Dijkstra’s Algorithm**      | `O((V + E) log V)`          | `O(V)` (distance array)    | Finds shortest paths from a source node in a graph with non-negative weights.   |
| **Bellman-Ford Algorithm**    | `O(V * E)`                  | `O(V)` (distance array)    | Finds shortest paths in graphs with negative weights; detects negative cycles.  |
| **Floyd-Warshall Algorithm**  | `O(V^3)`                   | `O(V^2)` (distance matrix) | Finds shortest paths between all pairs of nodes.                                |
| **Prim’s Algorithm (MST)**    | `O(E log V)`                | `O(V)` (priority queue)    | Builds a minimum spanning tree using a priority queue.                          |
| **Kruskal’s Algorithm (MST)** | `O(E log E)`                | `O(E + V)` (union-find)    | Builds a minimum spanning tree by sorting edges and checking for cycles.        |
| **Topological Sort (Kahn)**   | `O(V + E)`                  | `O(V)` (queue, in-degree)  | Orders vertices in a directed acyclic graph (DAG).                              |
| **Topological Sort (DFS)**    | `O(V + E)`                  | `O(V)` (recursion stack)   | Orders vertices in a DAG using depth-first traversal.                           |
```

**Explanation of Symbols:**

- `V`: Number of vertices in the graph.
- `E`: Number of edges in the graph.
- Space complexity includes additional structures like queues, stacks, or arrays required for the algorithms.

This table provides a quick and clear reference for comparing algorithm complexities.