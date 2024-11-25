# Greedy

**Greedy algorithms** are a problem-solving approach where decisions are made sequentially, choosing the locally optimal choice at each step with the hope of finding a global optimum. Greedy algorithms are straightforward and often efficient, but they only work for certain types of problems where choosing a local optimum guarantees a globally optimal solution.

### Key Concepts of Greedy Algorithms

1. **Greedy Choice Property**: The choice that looks the best at the moment (locally optimal choice) can be extended to an optimal solution for the entire problem.
2. **Optimal Substructure**: A problem has an optimal substructure if an optimal solution to the problem contains optimal solutions to its subproblems.

When both these properties are present, a greedy approach can produce an optimal solution.

---

### Common Types of Problems Solved by Greedy Algorithms

1. **Interval Scheduling (Activity Selection)**
2. **Fractional Knapsack Problem**
3. **Minimum Spanning Tree (MST)**
4. **Huffman Coding (Compression)**
5. **Dijkstra’s Shortest Path Algorithm**
6. **Job Sequencing with Deadlines**

Let’s explore these problems, with examples and solutions, to understand how greedy algorithms work.

---

### 1. **Interval Scheduling (Activity Selection Problem)**

**Problem**: Given a list of activities with their start and end times, select the maximum number of activities that don’t overlap.

**Example**:
```
Input: Activities = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]
Output: [(1, 4), (5, 7), (8, 9)]
```

**Greedy Solution**:
- Sort the activities by their end times.
- Select the activity with the earliest end time that does not overlap with the previously selected activity.
  
**Steps**:
1. Sort activities based on their end times.
2. Initialize an empty list for the selected activities.
3. For each activity, if its start time is after or at the end time of the last selected activity, add it to the selected activities.

**Code Example**:

```python
def activity_selection(activities):
    # Sort activities by end time
    activities.sort(key=lambda x: x[1])
    
    selected_activities = []
    last_end_time = 0
    
    for activity in activities:
        start, end = activity
        if start >= last_end_time:
            selected_activities.append(activity)
            last_end_time = end
    
    return selected_activities
```

**Time Complexity**: O(n log n) due to sorting.

**Explanation**:
- The greedy choice property holds because selecting the activity that finishes the earliest leaves the maximum room for other activities, maximizing the number of activities.

---

### 2. **Fractional Knapsack Problem**

**Problem**: Given a set of items with weights and values, find the maximum value that can be obtained with a knapsack of capacity `W`. You can take fractions of items.

**Example**:
```
Input: Items = [(value=60, weight=10), (value=100, weight=20), (value=120, weight=30)], Capacity = 50
Output: 240 (take all of item 1, all of item 2, and 2/3 of item 3)
```

**Greedy Solution**:
- Calculate the value-to-weight ratio for each item.
- Sort items by this ratio in descending order.
- Take as much of each item as possible, starting with the highest ratio, until the knapsack is full.

**Code Example**:

```python
def fractional_knapsack(items, capacity):
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    
    total_value = 0
    for value, weight in items:
        if capacity >= weight:
            total_value += value
            capacity -= weight
        else:
            total_value += value * (capacity / weight)
            break
    
    return total_value
```

**Time Complexity**: O(n log n) for sorting.

**Explanation**:
- The greedy choice property works here because taking items with the highest value-to-weight ratio maximizes the total value.

---

### 3. **Minimum Spanning Tree (MST)**

The **Minimum Spanning Tree** is a subgraph of an undirected, weighted graph that connects all vertices with the minimum possible total edge weight.

#### Kruskal's Algorithm

**Kruskal’s Algorithm** is a greedy algorithm for finding the MST:
- Sort all edges in ascending order of their weights.
- Add edges to the MST one by one, starting from the smallest, and skip edges that would create a cycle.

**Steps**:
1. Sort edges by weight.
2. Initialize an empty list for the MST.
3. For each edge, add it to the MST if it doesn’t form a cycle with already selected edges.

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
    mst = []
    
    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):
            mst.append((u, v, weight))
            ds.union(u, v)
    
    return mst
```

**Time Complexity**: O(E log E) for sorting edges.

**Explanation**:
- The greedy choice property is evident since selecting the smallest edge at each step guarantees the minimum weight MST without forming cycles.

---

### 4. **Huffman Coding**

**Problem**: Given a set of characters and their frequencies, construct a binary tree that minimizes the weighted path length (used in file compression).

**Example**:
```
Input: Characters = ['a', 'b', 'c', 'd'], Frequencies = [5, 9, 12, 13]
Output: Huffman encoding tree with minimal cost.
```

**Greedy Solution**:
- Use a priority queue (Min-Heap) to build a tree with minimal weighted path length by combining the two nodes with the smallest frequency at each step.

**Steps**:
1. Create a Min-Heap of nodes, each representing a character and its frequency.
2. Remove two nodes with the smallest frequency and create a new node with their combined frequency.
3. Repeat until there is only one node left.

**Code Example**:

```python
import heapq

def huffman_encoding(char_freq):
    heap = [[weight, [char, ""]] for char, weight in char_freq.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

# Example input
char_freq = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16}
print(huffman_encoding(char_freq))
```

**Time Complexity**: O(n log n), as each heap operation takes log n.

**Explanation**:
- Huffman coding is based on the greedy choice of combining the least frequent nodes to minimize the total cost.

---

### Summary of Greedy Algorithm Problems

| **Problem**                       | **Greedy Choice**                                             | **Complexity**           |
|-----------------------------------|---------------------------------------------------------------|--------------------------|
| **Activity Selection**            | Select activity with the earliest finish time                | O(n log n)               |
| **Fractional Knapsack**           | Select items with the highest value-to-weight ratio          | O(n log n)               |
| **Kruskal's MST**                 | Select edges with the smallest weight that don’t form cycles | O(E log E)               |
| **Huffman Coding**                | Combine nodes with the lowest frequency                       | O(n log n)               |

Greedy algorithms are effective and efficient for certain problems, especially when they have **optimal substructure** and **greedy choice property**. However, they may not work for problems that require exploring multiple paths, where dynamic programming or backtracking might be necessary.