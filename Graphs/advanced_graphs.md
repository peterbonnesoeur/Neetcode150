# Advanced graphs

Advanced graph algorithms extend beyond basic traversal and shortest path finding. These algorithms tackle complex problems like finding cycles, detecting strongly connected components, optimizing flow through networks, and solving probabilistic pathfinding. Here are some advanced graph concepts and algorithms commonly used in more specialized areas of software engineering, computer science, and operations research:

### 1. Strongly Connected Components (SCC)

In a **directed graph**, a **strongly connected component** (SCC) is a maximal subgraph where every pair of vertices is reachable from each other. Identifying SCCs is useful in applications such as compiler optimization, deadlock detection, and network analysis.

#### Kosaraju’s Algorithm

**Description**: Kosaraju’s algorithm finds all SCCs in a directed graph in O(V + E) time using two depth-first searches (DFS) and a stack.

**Steps**:
1. Perform DFS on the original graph and push each vertex onto a stack after it finishes.
2. Reverse the direction of all edges in the graph.
3. Perform DFS on the reversed graph in the order of vertices in the stack, collecting SCCs.

**Code Example**:

```python
def kosaraju_scc(graph, V):
    # Step 1: Fill the stack with nodes in finishing order
    def dfs(v):
        visited[v] = True
        for neighbor in graph[v]:
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(v)

    # Step 2: Transpose the graph
    def transpose_graph():
        transposed = [[] for _ in range(V)]
        for v in range(V):
            for neighbor in graph[v]:
                transposed[neighbor].append(v)
        return transposed

    # Step 3: Collect SCCs in the transposed graph
    def dfs_transposed(v):
        visited[v] = True
        component.append(v)
        for neighbor in transposed_graph[v]:
            if not visited[neighbor]:
                dfs_transposed(neighbor)

    # Fill stack with finish times
    visited = [False] * V
    stack = []
    for i in range(V):
        if not visited[i]:
            dfs(i)

    # Transpose the graph
    transposed_graph = transpose_graph()

    # DFS on transposed graph in stack order
    visited = [False] * V
    sccs = []
    while stack:
        v = stack.pop()
        if not visited[v]:
            component = []
            dfs_transposed(v)
            sccs.append(component)

    return sccs
```

**Time Complexity**: O(V + E)

---

### 2. Maximum Flow (Ford-Fulkerson & Edmonds-Karp Algorithms)

**Maximum Flow** is the maximum amount of flow that can be pushed from a source node to a sink node in a flow network, where each edge has a capacity.

#### Ford-Fulkerson Algorithm

**Description**: The Ford-Fulkerson algorithm computes the maximum flow by repeatedly finding augmenting paths and adding flow along these paths.

**Steps**:
1. Start with zero flow.
2. While there’s an augmenting path from source to sink with remaining capacity, increase flow along the path.
3. Use DFS or BFS to find augmenting paths.

**Code Example** (BFS for finding paths, also known as Edmonds-Karp algorithm):

```python
from collections import deque

def bfs(capacity, flow, source, sink, parent):
    visited = set()
    queue = deque([source])
    visited.add(source)

    while queue:
        u = queue.popleft()
        for v in range(len(capacity)):
            if v not in visited and capacity[u][v] - flow[u][v] > 0:  # remaining capacity
                parent[v] = u
                visited.add(v)
                queue.append(v)
                if v == sink:
                    return True
    return False

def ford_fulkerson(capacity, source, sink):
    V = len(capacity)
    flow = [[0] * V for _ in range(V)]
    parent = [-1] * V
    max_flow = 0

    while bfs(capacity, flow, source, sink, parent):
        path_flow = float('Inf')
        s = sink

        while s != source:
            path_flow = min(path_flow, capacity[parent[s]][s] - flow[parent[s]][s])
            s = parent[s]

        v = sink
        while v != source:
            u = parent[v]
            flow[u][v] += path_flow
            flow[v][u] -= path_flow
            v = parent[v]

        max_flow += path_flow

    return max_flow
```

**Time Complexity**:
- **Edmonds-Karp**: O(V * E^2) using BFS for finding augmenting paths.

---

### 3. Minimum Cut

The **minimum cut** of a graph is the smallest set of edges that, if removed, would disconnect the source from the sink. This is closely related to maximum flow, as the max-flow min-cut theorem states that the maximum flow in a flow network is equal to the total weight of the edges in a minimum cut.

**Approach**:
- Use Ford-Fulkerson or Edmonds-Karp to find maximum flow.
- Find all reachable nodes from the source in the residual graph, and edges connecting these to non-reachable nodes are part of the minimum cut.

**Application**: Minimum cuts are used in image segmentation, network reliability, and clustering.

---

### 4. All-Pairs Shortest Path (Floyd-Warshall Algorithm)

**Description**: Floyd-Warshall finds the shortest paths between all pairs of vertices in a weighted graph, including handling negative weights (but not negative cycles).

**Code Example**:

```python
def floyd_warshall(graph, V):
    dist = [[float('inf')] * V for _ in range(V)]
    for u in range(V):
        dist[u][u] = 0

    for u, v, weight in graph:
        dist[u][v] = weight

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist
```

**Time Complexity**: O(V^3)

---

### 5. A* Search Algorithm

**Description**: A* is a pathfinding algorithm that uses heuristics to guide its search, aiming to find the shortest path more efficiently than Dijkstra’s. It’s commonly used in games and AI for navigation.

**Heuristic Function**: A* uses a heuristic function `h(n)` that estimates the cost to reach the target from node `n`.

**Code Example** (with a simple Manhattan distance heuristic for a grid):

```python
from heapq import heappop, heappush

def a_star(graph, start, goal, heuristic):
    open_set = []
    heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_set:
        _, current = heappop(open_set)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        for neighbor, weight in graph[current]:
            tentative_g_score = g_score[current] + weight
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                heappush(open_set, (f_score[neighbor], neighbor))

    return None  # Path not found
```

**Time Complexity**: Depends on the heuristic but generally O(E).

---

### 6. Cycle Detection in Directed and Undirected Graphs

Cycle detection is essential for understanding dependencies, deadlock detection, and ensuring acyclic properties in graphs.

#### For Directed Graphs

**Algorithm**: Use DFS with a recursion stack to detect cycles in directed graphs.

**Code Example**:

```python
def detect_cycle_directed(graph, V):
    visited = [False] * V
    rec_stack = [False] * V

    def dfs(v):
        visited[v] = True
        rec_stack[v] = True

        for neighbor in graph[v]:
            if not visited[neighbor] and dfs(neighbor):
                return True
            elif rec_stack[neighbor]:
                return True

        rec_stack[v] = False
        return False

    for node in range(V):
        if not visited[node] and dfs(node):
            return True
    return False
```

#### For Undirected Graphs

**Algorithm**: Use DFS, ensuring you don’t backtrack to the immediate parent.

**Code Example**:

```python
def detect_cycle_undirected(graph, V):
    visited = [False] * V

    def dfs(v, parent):
        visited[v] = True
        for neighbor in graph[v]:
            if not visited[neighbor]:
                if dfs(neighbor, v):
                    return True
            elif neighbor != parent:
                return True
        return False

    for node in range(V):
        if not visited[node] and dfs(node, -1):
            return True
    return False
```

**Time Complexity**: O(V + E) for both algorithms.

---

### 7. Traveling Salesman Problem (TSP)

The **Traveling Salesman Problem** (TSP) is a classic optimization problem that seeks the shortest possible route visiting each city exactly once and returning to the