# Heap and priority queue

- [Heap and priority queue](#heap-and-priority-queue)
  - [Heap](#heap)
    - [Heap to Array Mapping](#heap-to-array-mapping)
    - [Example of a Min-Heap and its Array Representation](#example-of-a-min-heap-and-its-array-representation)
      - [Array Representation:](#array-representation)
    - [Visualizing Array-Based Heap Structure:](#visualizing-array-based-heap-structure)
      - [Tree Structure:](#tree-structure)
      - [Array Structure:](#array-structure)
    - [Node Relationships in the Array:](#node-relationships-in-the-array)
    - [Example of a Max-Heap and its Array Representation](#example-of-a-max-heap-and-its-array-representation)
      - [Array Representation:](#array-representation-1)
      - [Visualizing the Array-Based Heap Structure:](#visualizing-the-array-based-heap-structure)
      - [Tree Structure:](#tree-structure-1)
      - [Array Structure:](#array-structure-1)
  - [What does a heap look like as an Array:](#what-does-a-heap-look-like-as-an-array)
    - [Heap to Array Mapping](#heap-to-array-mapping-1)
    - [Example of a Min-Heap and its Array Representation](#example-of-a-min-heap-and-its-array-representation-1)
      - [Array Representation:](#array-representation-2)
    - [Visualizing Array-Based Heap Structure:](#visualizing-array-based-heap-structure-1)
      - [Tree Structure:](#tree-structure-2)
      - [Array Structure:](#array-structure-2)
    - [Node Relationships in the Array:](#node-relationships-in-the-array-1)
    - [Example of a Max-Heap and its Array Representation](#example-of-a-max-heap-and-its-array-representation-1)
      - [Array Representation:](#array-representation-3)
  - [When you perform a **`heappop`** operation on a **heap**, the following steps occur:](#when-you-perform-a-heappop-operation-on-a-heap-the-following-steps-occur)
    - [Initial Min-Heap (Array Representation)](#initial-min-heap-array-representation)
    - [Step 1: Remove the Root](#step-1-remove-the-root)
    - [Step 2: Replace the Root with the Last Element](#step-2-replace-the-root-with-the-last-element)
    - [Step 3: Heapify Down (Restore Heap Property)](#step-3-heapify-down-restore-heap-property)
    - [Final Min-Heap after `heappop`](#final-min-heap-after-heappop)
    - [Summary of Steps in `heappop`:](#summary-of-steps-in-heappop)
    - [Time Complexity:](#time-complexity)
  - [What does the heapify process does](#what-does-the-heapify-process-does)
    - [Array to Heapify (Unsorted Array)](#array-to-heapify-unsorted-array)
    - [Heapify Process Overview:](#heapify-process-overview)
    - [Step-by-Step Heapify Process:](#step-by-step-heapify-process)
      - [**Step 1: Heapify Node at Index 4 (Value = 14)**](#step-1-heapify-node-at-index-4-value--14)
      - [**Step 2: Heapify Node at Index 3 (Value = 10)**](#step-2-heapify-node-at-index-3-value--10)
      - [**Step 3: Heapify Node at Index 2 (Value = 42)**](#step-3-heapify-node-at-index-2-value--42)
      - [**Step 4: Heapify Node at Index 1 (Value = 33)**](#step-4-heapify-node-at-index-1-value--33)
      - [**Step 5: Heapify Node at Index 0 (Value = 35)**](#step-5-heapify-node-at-index-0-value--35)
    - [Final Min-Heap after Heapify:](#final-min-heap-after-heapify)
    - [Summary of Steps in Heapify:](#summary-of-steps-in-heapify)
    - [Time Complexity of Heapify:](#time-complexity-of-heapify)


## Heap

A **heap** can be efficiently represented as an array (or list) due to its **complete binary tree** structure. In a heap, each level of the tree is filled from left to right, which makes it possible to store the tree in a linear array without requiring pointers or additional storage.

### Heap to Array Mapping

In an array-based representation of a binary heap:
- **The root node** is at index `0`.
- **The parent** of a node at index `i` is at index `(i - 1) // 2`.
- **The left child** of a node at index `i` is at index `2 * i + 1`.
- **The right child** of a node at index `i` is at index `2 * i + 2`.

Let’s look at an example.

### Example of a Min-Heap and its Array Representation

Suppose we have the following **Min-Heap**:

```
        10
       /  \
     15    20
    /  \   /  
   30  40 50
```

This is a valid Min-Heap because the value of every node is smaller than or equal to its children.

#### Array Representation:
```
Index:   0   1   2   3   4   5
Array: [10, 15, 20, 30, 40, 50]
```

**Array Explanation:**
1. The root (`10`) is at index `0`.
2. The left child of `10` is `15` (at index `1`), and the right child is `20` (at index `2`).
3. The left and right children of `15` (at index `1`) are `30` (at index `3`) and `40` (at index `4`).
4. The left child of `20` (at index `2`) is `50` (at index `5`), and since there is no right child for `20`, the heap is complete.

### Visualizing Array-Based Heap Structure:

#### Tree Structure:
```
        10                <-- Root (index 0)
       /  \
     15    20             <-- Level 1 (indices 1, 2)
    /  \   /  
   30  40 50              <-- Level 2 (indices 3, 4, 5)
```

#### Array Structure:
```
[10, 15, 20, 30, 40, 50]
```

### Node Relationships in the Array:

For a node at index `i`:
- The **parent** is at index `(i - 1) // 2`:
  - For `i = 1` (node `15`), the parent is at index `(1 - 1) // 2 = 0` (node `10`).
  - For `i = 2` (node `20`), the parent is at index `(2 - 1) // 2 = 0` (node `10`).
- The **left child** is at index `2 * i + 1`:
  - For `i = 0` (node `10`), the left child is at index `2 * 0 + 1 = 1` (node `15`).
  - For `i = 1` (node `15`), the left child is at index `2 * 1 + 1 = 3` (node `30`).
- The **right child** is at index `2 * i + 2`:
  - For `i = 0` (node `10`), the right child is at index `2 * 0 + 2 = 2` (node `20`).
  - For `i = 1` (node `15`), the right child is at index `2 * 1 + 2 = 4` (node `40`).

---

### Example of a Max-Heap and its Array Representation

Suppose we have the following **Max-Heap**:

```
        50
       /  \
     30    40
    /  \   /  
   10  15 20
```

This is a valid Max-Heap because the value of every node is larger than or equal to its children.

#### Array Representation:
```
Index:   0   1   2   3   4   5
Array: [50, 30, 40, 10, 15, 20]
```

**Array Explanation:**
1. The root (`50`) is at index `0`.
2. The left child of `50` is `30` (at index `1`), and the right child is `40` (at index `2`).
3. The left and right children of `30` (at index `1`) are `10` (at index `3`) and `15` (at index `4`).
4. The left child of `40` (at index `2`) is `20` (at index `5`), and since there is no right child for `40`, the heap is complete.

#### Visualizing the Array-Based Heap Structure:

#### Tree Structure:
```
        50                <-- Root (index 0)
       /  \
     30    40             <-- Level 1 (indices 1, 2)
    /  \   /  
   10  15 20              <-- Level 2 (indices 3, 4, 5)
```

#### Array Structure:
```
[50, 30, 40, 10, 15, 20]
```

#Questions
## What does a heap look like as an Array:

A **heap** can be efficiently represented as an array (or list) due to its **complete binary tree** structure. In a heap, each level of the tree is filled from left to right, which makes it possible to store the tree in a linear array without requiring pointers or additional storage.

### Heap to Array Mapping

In an array-based representation of a binary heap:
- **The root node** is at index `0`.
- **The parent** of a node at index `i` is at index `(i - 1) // 2`.
- **The left child** of a node at index `i` is at index `2 * i + 1`.
- **The right child** of a node at index `i` is at index `2 * i + 2`.

Let’s look at an example.

### Example of a Min-Heap and its Array Representation

Suppose we have the following **Min-Heap**:

```
        10
       /  \
     15    20
    /  \   /  
   30  40 50
```

This is a valid Min-Heap because the value of every node is smaller than or equal to its children.

#### Array Representation:
```
Index:   0   1   2   3   4   5
Array: [10, 15, 20, 30, 40, 50]
```

**Array Explanation:**
1. The root (`10`) is at index `0`.
2. The left child of `10` is `15` (at index `1`), and the right child is `20` (at index `2`).
3. The left and right children of `15` (at index `1`) are `30` (at index `3`) and `40` (at index `4`).
4. The left child of `20` (at index `2`) is `50` (at index `5`), and since there is no right child for `20`, the heap is complete.

### Visualizing Array-Based Heap Structure:

#### Tree Structure:
```
        10                <-- Root (index 0)
       /  \
     15    20             <-- Level 1 (indices 1, 2)
    /  \   /  
   30  40 50              <-- Level 2 (indices 3, 4, 5)
```

#### Array Structure:
```
[10, 15, 20, 30, 40, 50]
```

### Node Relationships in the Array:

For a node at index `i`:
- The **parent** is at index `(i - 1) // 2`:
  - For `i = 1` (node `15`), the parent is at index `(1 - 1) // 2 = 0` (node `10`).
  - For `i = 2` (node `20`), the parent is at index `(2 - 1) // 2 = 0` (node `10`).
- The **left child** is at index `2 * i + 1`:
  - For `i = 0` (node `10`), the left child is at index `2 * 0 + 1 = 1` (node `15`).
  - For `i = 1` (node `15`), the left child is at index `2 * 1 + 1 = 3` (node `30`).
- The **right child** is at index `2 * i + 2`:
  - For `i = 0` (node `10`), the right child is at index `2 * 0 + 2 = 2` (node `20`).
  - For `i = 1` (node `15`), the right child is at index `2 * 1 + 2 = 4` (node `40`).

---

### Example of a Max-Heap and its Array Representation

Suppose we have the following **Max-Heap**:

```
        50
       /  \
     30    40
    /  \   /  
   10  15 20
```

This is a valid Max-Heap because the value of every node is larger than or equal to its children.

#### Array Representation:
```
Index:   0   1   2   3   4   5
Array: [50, 30, 40, 10, 15, 20]
```

**Array Explanation:**
1. The root (`50`) is at index `0`.
2. The left child of `50` is `30` (at index `1`), and the right child is `40` (at index `2`).
3. The left and right children of `30` (at index `1`) are `10` (at index `3`) and `15` (at index `4`).
4. The left child of `40` (at index `2`) is `20` (at index `5`), and since there is no right child for `40`, the heap is complete.


## When you perform a **`heappop`** operation on a **heap**, the following steps occur:

1. **Remove the Root**: The root element (the smallest element in a Min-Heap or the largest in a Max-Heap) is removed because it has the highest priority.
2. **Replace the Root**: The last element in the heap (in the array representation) is moved to the root position. This temporarily violates the heap property.
3. **Heapify Down**: The heap is restructured by comparing the new root with its children and swapping it with the smallest child (in a Min-Heap) or the largest child (in a Max-Heap) until the heap property is restored.

Let's go through a step-by-step example of how **`heappop`** works on a Min-Heap:

### Initial Min-Heap (Array Representation)
```
Heap as Tree:
        10
       /  \
     15    20
    /  \   /  
   30  40 50  

Heap as Array: [10, 15, 20, 30, 40, 50]
```

In this case, the Min-Heap property is satisfied, as each parent node is smaller than its children. Now, let's perform the `heappop` operation on this heap.

### Step 1: Remove the Root
The root node, `10`, is the smallest element in the heap, so it will be removed.

**Array after removing the root (before replacing the root):**
```
[15, 20, 30, 40, 50]
```

### Step 2: Replace the Root with the Last Element
The last element in the heap, `50`, is moved to the root position to fill the gap left by the removed root. Now, the heap temporarily violates the Min-Heap property because `50` is larger than its children.

**Heap after replacing the root with `50`:**
```
        50
       /  \
     15    20
    /  \   
   30  40  

Heap as Array: [50, 15, 20, 30, 40]
```

### Step 3: Heapify Down (Restore Heap Property)
Now we perform **heapify down** to restore the Min-Heap property:
- Compare the new root (`50`) with its children (`15` and `20`).
- Since `15` is the smallest child, we swap `50` with `15`.

**Heap after first swap:**
```
        15
       /  \
     50    20
    /  \   
   30  40  

Heap as Array: [15, 50, 20, 30, 40]
```

Next, we continue heapifying down:
- Compare `50` (now at index 1) with its children (`30` and `40`).
- `30` is the smallest child, so we swap `50` with `30`.

**Heap after second swap:**
```
        15
       /  \
     30    20
    /  \   
   50  40  

Heap as Array: [15, 30, 20, 50, 40]
```

Now the heap property is restored, and no further swaps are necessary.

### Final Min-Heap after `heappop`
```
Heap as Tree:
        15
       /  \
     30    20
    /  \   
   50  40  

Heap as Array: [15, 30, 20, 50, 40]
```

The new root is `15`, which is now the smallest element, and the Min-Heap property is satisfied again.

### Summary of Steps in `heappop`:
1. **Remove the root** (`10` in our case).
2. **Replace the root** with the last element (`50`).
3. **Heapify down** to restore the heap property:
   - Swap `50` with `15` (its smallest child).
   - Swap `50` with `30` (its smallest child).
4. The heap is now a valid Min-Heap again.

### Time Complexity:
The time complexity of `heappop` is **O(log n)**, where `n` is the number of elements in the heap. This is because in the worst case, we might have to perform log n swaps as we traverse from the root to the leaf node.

## What does the heapify process does

Let’s walk through the **heapify process** on an unsorted array to turn it into a **valid heap**. Heapifying an array means arranging the elements so that they satisfy the heap property. For the purpose of this example, we'll convert an unsorted array into a **Min-Heap**.

### Array to Heapify (Unsorted Array)
```
Array: [35, 33, 42, 10, 14, 19, 27, 44, 26, 31]
```

### Heapify Process Overview:
Heapify is generally performed in two phases:
1. **Build a Heap**: Start from the last non-leaf node and call the `heapify down` process on each node, moving upwards.
2. **Heapify Down**: For each node, swap it with its smallest child if the heap property is violated (for Min-Heap).

**Heapify starts from the last non-leaf node**, which is found at index `(n // 2 - 1)` where `n` is the length of the array.

### Step-by-Step Heapify Process:

**Initial Array:**
```
[35, 33, 42, 10, 14, 19, 27, 44, 26, 31]
```

The last non-leaf node is at index `(10 // 2 - 1) = 4` (node `14`).

---

#### **Step 1: Heapify Node at Index 4 (Value = 14)**

- **Node:** `14` (index 4)
- **Left child:** `31` (index 9)
- **Right child:** N/A (no right child)

**Comparison**:
- Since `14` is smaller than its only child `31`, no swap is needed.

**Heap after Step 1:**
```
[35, 33, 42, 10, 14, 19, 27, 44, 26, 31]
```

---

#### **Step 2: Heapify Node at Index 3 (Value = 10)**

- **Node:** `10` (index 3)
- **Left child:** `44` (index 7)
- **Right child:** `26` (index 8)

**Comparison**:
- `10` is smaller than both `44` and `26`, so no swap is needed.

**Heap after Step 2:**
```
[35, 33, 42, 10, 14, 19, 27, 44, 26, 31]
```

---

#### **Step 3: Heapify Node at Index 2 (Value = 42)**

- **Node:** `42` (index 2)
- **Left child:** `19` (index 5)
- **Right child:** `27` (index 6)

**Comparison**:
- `42` is larger than both `19` and `27`.
- Swap `42` with the smaller child, `19`.

**Heap after first swap (index 2 <-> 5):**
```
[35, 33, 19, 10, 14, 42, 27, 44, 26, 31]
```

Now, we need to heapify the subtree rooted at index 5.

- **Node:** `42` (index 5)
- **Children:** N/A (no children)

Since there are no children, no further action is needed.

**Heap after Step 3:**
```
[35, 33, 19, 10, 14, 42, 27, 44, 26, 31]
```

---

#### **Step 4: Heapify Node at Index 1 (Value = 33)**

- **Node:** `33` (index 1)
- **Left child:** `10` (index 3)
- **Right child:** `14` (index 4)

**Comparison**:
- `33` is larger than both `10` and `14`.
- Swap `33` with the smallest child, `10`.

**Heap after first swap (index 1 <-> 3):**
```
[35, 10, 19, 33, 14, 42, 27, 44, 26, 31]
```

Now, we need to heapify the subtree rooted at index 3.

- **Node:** `33` (index 3)
- **Left child:** `44` (index 7)
- **Right child:** `26` (index 8)

**Comparison**:
- `33` is smaller than both children, so no swap is needed.

**Heap after Step 4:**
```
[35, 10, 19, 33, 14, 42, 27, 44, 26, 31]
```

---

#### **Step 5: Heapify Node at Index 0 (Value = 35)**

- **Node:** `35` (index 0)
- **Left child:** `10` (index 1)
- **Right child:** `19` (index 2)

**Comparison**:
- `35` is larger than both `10` and `19`.
- Swap `35` with the smallest child, `10`.

**Heap after first swap (index 0 <-> 1):**
```
[10, 35, 19, 33, 14, 42, 27, 44, 26, 31]
```

Now, we need to heapify the subtree rooted at index 1.

- **Node:** `35` (index 1)
- **Left child:** `33` (index 3)
- **Right child:** `14` (index 4)

**Comparison**:
- `35` is larger than `14`.
- Swap `35` with `14`.

**Heap after second swap (index 1 <-> 4):**
```
[10, 14, 19, 33, 35, 42, 27, 44, 26, 31]
```

Now, we need to heapify the subtree rooted at index 4.

- **Node:** `35` (index 4)
- **Left child:** `31` (index 9)
- **Right child:** N/A

**Comparison**:
- `35` is larger than `31`.
- Swap `35` with `31`.

**Heap after third swap (index 4 <-> 9):**
```
[10, 14, 19, 33, 31, 42, 27, 44, 26, 35]
```

No further heapifying is needed because node `35` has no children.

---

### Final Min-Heap after Heapify:
```
        10
       /  \
     14    19
    /  \   /  \
   33  31 42  27
  /  \ 
 44  35

Heap as Array: [10, 14, 19, 33, 31, 42, 27, 44, 26, 35]
```

### Summary of Steps in Heapify:

1. Start from the last non-leaf node (`index 4`) and work upwards.
2. Apply **Heapify Down** (or sift down) to each node to maintain the heap property.
3. After processing all nodes, the array is transformed into a valid **Min-Heap**.

### Time Complexity of Heapify:
- **Heapify Down** for each node takes **O(log n)** time, where `n` is the number of elements below that node.
- The overall complexity of converting an array into a heap using **Heapify** is **O(n)** because you are starting from the bottom of the tree, where fewer elements need to be heapified (for example, leaves don’t need heapifying).

Would you like more examples or an explanation of how heapify works for a Max-Heap?