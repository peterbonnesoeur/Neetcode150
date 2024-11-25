### Tree Problems Overview

Trees are a fundamental data structure in computer science, and one of the most common tree types is the **Binary Search Tree (BST)**. In addition to basic operations like insertion and deletion, we often need to perform tree traversal techniques like **Depth-First Search (DFS)** and **Breadth-First Search (BFS)** to explore nodes, solve problems, and implement algorithms. Let’s dive into key tree operations, focusing on the **Binary Search Tree (BST)** and traversal strategies, along with their complexity and use cases.

---

## 1. **Binary Search Tree (BST) Insert and Remove**

A **Binary Search Tree** (BST) is a binary tree where each node has:
- A **left child** that contains values less than the parent node.
- A **right child** that contains values greater than the parent node.

### Insert Operation in BST

To insert a node into a BST, you follow the **binary search property** and recursively or iteratively place the new node in the correct position.

#### Recursive Insert:

```python
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def insert_bst(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root
```

**Steps**:
- Start at the root.
- Compare the value to insert with the root’s value.
- If the value is smaller, move left; if it is larger, move right.
- Insert the value when you find an empty spot (i.e., `None`).

**Time Complexity**:
- **Best/Average Case**: O(log n) for balanced trees (as you halve the search space at each step).
- **Worst Case**: O(n) for skewed trees (like inserting in a sorted order, creating a linked list).

#### Iterative Insert:

```python
def insert_bst_iterative(root, val):
    if root is None:
        return TreeNode(val)
    
    current = root
    while current:
        if val < current.val:
            if current.left is None:
                current.left = TreeNode(val)
                break
            current = current.left
        else:
            if current.right is None:
                current.right = TreeNode(val)
                break
            current = current.right
    return root
```

**Pattern**: Both recursive and iterative insertion techniques rely on binary search, navigating left or right based on comparisons.

### Remove Operation in BST

The remove operation in a BST is more complex because it has to maintain the BST property after the removal. There are three possible cases:
1. **Node to be removed is a leaf** (no children).
2. **Node to be removed has one child** (left or right).
3. **Node to be removed has two children** (left and right).

#### Recursive Remove:

```python
def remove_bst(root, val):
    if root is None:
        return None
    
    if val < root.val:
        root.left = remove_bst(root.left, val)
    elif val > root.val:
        root.right = remove_bst(root.right, val)
    else:  # Node found
        if not root.left:  # Case 1 & 2: No left child
            return root.right
        if not root.right:  # Case 1 & 2: No right child
            return root.left
        
        # Case 3: Two children
        min_larger_node = find_min(root.right)  # Find the smallest node in the right subtree
        root.val = min_larger_node.val  # Replace the current node's value with the successor's value
        root.right = remove_bst(root.right, min_larger_node.val)  # Delete the successor
        
    return root

def find_min(node):
    while node.left:
        node = node.left
    return node
```

**Time Complexity**:
- **Best/Average Case**: O(log n) for balanced trees.
- **Worst Case**: O(n) for skewed trees.

---

## 2. **Depth First Search (DFS)**

**DFS** is a tree/graph traversal technique where you explore as far along a branch as possible before backtracking. It can be implemented in three common orders for binary trees:
- **Pre-order** (Root, Left, Right)
- **In-order** (Left, Root, Right)
- **Post-order** (Left, Right, Root)

### Recursive DFS (In-Order Traversal Example):

```python
def in_order_dfs(root):
    if root:
        in_order_dfs(root.left)
        print(root.val)  # Process the root
        in_order_dfs(root.right)
```

### Iterative DFS (Using Stack):

Instead of recursion, DFS can also be implemented iteratively using an explicit **stack**.

```python
def iterative_in_order_dfs(root):
    stack = []
    current = root
    
    while current or stack:
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        print(current.val)  # Process the root
        current = current.right
```

### Use Cases:
- **In-Order**: Used for BST traversal to get the elements in sorted order.
- **Pre-Order**: Useful for creating a copy of the tree or in prefix expression evaluation.
- **Post-Order**: Used in deleting or freeing nodes in memory.

**Time Complexity**: O(n) for all DFS variants, where `n` is the number of nodes in the tree.

**Space Complexity**: O(h), where `h` is the height of the tree (worst case O(n) in unbalanced trees and O(log n) in balanced trees).

---

## 3. **Breadth First Search (BFS)**

**BFS** explores all the nodes at the present depth before moving on to the nodes at the next depth level. It is typically implemented using a **queue** (FIFO).

### Iterative BFS (Level Order Traversal):

```python
from collections import deque

def bfs_level_order(root):
    if not root:
        return
    
    queue = deque([root])
    while queue:
        node = queue.popleft()  # Dequeue the front node
        print(node.val)  # Process the node
        if node.left:
            queue.append(node.left)  # Enqueue the left child
        if node.right:
            queue.append(node.right)  # Enqueue the right child
```

### Use Cases:
- **Level Order Traversal**: BFS is naturally suited for problems requiring a level-wise exploration of nodes, such as finding the shortest path in an unweighted graph, or determining the minimum depth of a binary tree.

**Time Complexity**: O(n), where `n` is the number of nodes in the tree.
  
**Space Complexity**: O(w), where `w` is the maximum width of the tree (maximum number of nodes at any level).

---

## 4. **BST Sets and Maps**

In many applications, **BST-based sets** and **maps** (dictionaries) are built on the underlying structure of balanced binary search trees like AVL or Red-Black Trees, allowing for logarithmic time complexity for common operations such as **insert**, **remove**, and **search**.

### Example of a BST-based Set:

A BST can be used to implement a set, where each node stores a unique value. Inserting, removing, and searching for elements in the set will follow the same rules as a BST.

### Example of a BST-based Map (Dictionary):

A BST can be extended to store key-value pairs, where the keys are used for comparison during traversal. This is how many dictionaries (maps) are implemented internally in systems where a balanced BST is used.

- **Insertion** and **lookup** are based on the key, with O(log n) time complexity for both balanced trees like AVL or Red-Black Trees.

---

## 5. **Iterative Depth First Search (DFS)**

While recursive DFS is straightforward, an iterative approach using a **stack** is often preferred in environments with limited stack space or where explicit control of recursion is needed.

### Iterative Pre-order DFS Example:

```python
def iterative_pre_order_dfs(root):
    if not root:
        return
    
    stack = [root]
    while stack:
        node = stack.pop()
        print(node.val)  # Process the node
        if node.right:
            stack.append(node.right)  # Push right child first
        if node.left:
            stack.append(node.left)  # Push left child next
```

### Use Cases:
- Iterative DFS is often used in graph traversal or in situations where recursion depth could become problematic.
  
**Time Complexity**: O(n) for traversing all nodes in the tree.

**Space Complexity**: O(h) for storing nodes on the stack, where `h` is the height of the tree (can be O(log n) for balanced trees or O(n) for skewed trees).

---

### Summary of Patterns and Complexity:

| **Operation**              | **Time Complexity** (Balanced BST) | **Time Complexity** (Unbalanced BST) |
|----------------------------|------------------------------------|-------------------------------------|
| **Insert (BST)**            | O(log n)                          | O(n)                                |
| **Remove (BST)**            | O(log n)                          | O(n)                                |
| **DFS (In-order, Pre-order)**| O(n)                              | O(n)                                |
| **BFS (Level Order)**       | O(n)                              | O(n