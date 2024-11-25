### Linked List
A **Linked List** is a linear data structure where elements, called **nodes**, are stored in a sequence. Each node contains two components:
1. **Data**: The value or the data the node holds.
2. **Next Pointer**: A reference (or pointer) to the next node in the list.

A **Singly Linked List** allows traversal in only one direction—from the head (first node) to the tail (last node), where the last node’s next pointer points to `null`.

**Basic Structure of a Singly Linked List Node:**

```python
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node
```

### Doubly Linked List
A **Doubly Linked List (DLL)** is a type of linked list where each node has an extra pointer, called the **previous pointer**, that points to the previous node in the sequence. This allows for bidirectional traversal—both forward and backward through the list.

**Basic Structure of a Doubly Linked List Node:**

```python
class DoublyListNode:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node
```

**Advantages of a Doubly Linked List:**
- **Bidirectional Traversal**: You can traverse the list in both directions, which is useful in many scenarios (e.g., iterating through the list backward).
- **Easier Deletion**: Deleting a node is easier because you have a direct reference to its previous node, eliminating the need for a second traversal.
  
**Disadvantages:**
- Requires extra memory to store the `prev` pointer.
- Slightly more complex than singly linked lists due to the additional pointer.

### Fast and Slow Pointers (Tortoise and Hare Technique)
The **Fast and Slow Pointers** technique, also known as the **Tortoise and Hare** algorithm, is a commonly used technique in linked lists to solve several problems efficiently.

In this technique:
- A **slow pointer** moves one step at a time.
- A **fast pointer** moves two steps at a time.

This simple approach has powerful applications in problems involving linked lists, especially when you need to detect cycles or find the middle node of a list.

### Key Applications of Fast and Slow Pointers

#### 1. **Detecting Cycles in a Linked List (Cycle Detection)**

**Problem:**
Given a linked list, determine if it contains a cycle (i.e., the list loops back on itself).

**Solution:**
Use the fast and slow pointers approach:
- Initialize both pointers at the head.
- Move the fast pointer two steps at a time and the slow pointer one step at a time.
- If there is a cycle, the fast pointer will eventually "lap" the slow pointer (i.e., both will point to the same node).
- If there’s no cycle, the fast pointer will reach the end (`null`) without meeting the slow pointer.

**Example:**

```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next  # slow moves one step
        fast = fast.next.next  # fast moves two steps
        if slow == fast:  # cycle detected
            return True
    return False
```

**Time Complexity:**
- O(n), where `n` is the number of nodes in the list, because both pointers traverse the list only once.

#### 2. **Finding the Middle of a Linked List**

**Problem:**
Given a singly linked list, find the middle node. If there are two middle nodes (in an even-length list), return the second one.

**Solution:**
Use the fast and slow pointers technique:
- Initialize both pointers at the head.
- Move the slow pointer one step at a time and the fast pointer two steps at a time.
- When the fast pointer reaches the end of the list, the slow pointer will be at the middle node.

**Example:**

```python
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next  # slow moves one step
        fast = fast.next.next  # fast moves two steps
    return slow  # slow is at the middle node
```

**Time Complexity:**
- O(n), where `n` is the number of nodes in the list.

#### 3. **Detecting the Start of the Cycle in a Linked List**

**Problem:**
If a cycle is detected in a linked list, determine the node where the cycle begins.

**Solution:**
Once a cycle is detected, reset one pointer (say the slow pointer) to the head of the list, while the other pointer (fast) remains where it met the slow pointer. Move both pointers one step at a time. The point where they meet again will be the start of the cycle.

**Example:**

```python
def detect_cycle_start(head):
    slow = fast = head
    
    # Detect if there's a cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None  # No cycle

    # Find the start of the cycle
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow  # Start of the cycle
```

**Time Complexity:**
- O(n), where `n` is the number of nodes in the list.

#### 4. **Checking if a Linked List is a Palindrome**

**Problem:**
Check if a linked list is a palindrome (reads the same forward and backward).

**Solution:**
- Use the fast and slow pointer technique to find the middle of the list.
- Reverse the second half of the list.
- Compare the first half with the reversed second half to check if they are equal.

**Example:**

```python
def reverse_list(head):
    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    return prev

def is_palindrome(head):
    if not head:
        return True
    
    # Find the middle using fast and slow pointers
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse the second half of the list
    second_half = reverse_list(slow)
    
    # Compare the first half with the reversed second half
    first_half = head
    while second_half:
        if first_half.data != second_half.data:
            return False
      first_half = first_half.next
        second_half = second_half.next
    
    return True
```

**Time Complexity:**
- O(n), where `n` is the number of nodes in the list.
  
---

In a **linked list**, basic operations include inserting, deleting, and searching for elements, as well as traversing the list. The time complexity of each operation depends on the position in the list where the operation is performed and whether the list is singly or doubly linked.

Let’s explore the key operations and their time complexity.

### 1. **Insertion**

Insertion in a linked list can happen in several places: at the head, tail, or in the middle. The operation involves creating a new node and adjusting pointers.

#### a) **Insert at the Head**
- Insert a new node as the first element in the list.
  
**Steps:**
1. Create a new node.
2. Point the new node’s `next` pointer to the current head.
3. Update the head to be the new node.

**Time Complexity:**  
- **O(1)**, because only a few pointer changes are required, regardless of the size of the list.

#### b) **Insert at the Tail**
- Insert a new node at the end of the list.

**Steps:**
1. Traverse the list to find the tail (last node).
2. Set the tail’s `next` pointer to the new node.
3. Set the new node’s `next` to `None` (or `null`).

**Time Complexity:**
- **O(n)**, where `n` is the number of nodes in the list. You must traverse the entire list to find the last node.

**Note:** In a **doubly linked list** with a pointer to the tail, insertion at the tail can be done in **O(1)** by directly modifying the tail’s `next` and the new node’s `prev`.

#### c) **Insert at a Specific Position**
- Insert a new node at a specific index `k` in the list.

**Steps:**
1. Traverse the list to the `k-1` node.
2. Adjust pointers to insert the new node at the correct position.

**Time Complexity:**
- **O(n)**, since you may need to traverse up to `n` nodes to find the position where the new node is inserted.

### 2. **Deletion**

Deletion in a linked list also depends on the node's position (head, tail, or middle).

#### a) **Delete from the Head**
- Remove the first node in the list.

**Steps:**
1. Set the head to be the next node of the current head.

**Time Complexity:**
- **O(1)**, because only the head pointer needs to be updated.

#### b) **Delete from the Tail**
- Remove the last node in the list.

**Steps:**
1. Traverse the list to the second-last node.
2. Set the second-last node’s `next` to `None`.

**Time Complexity:**
- **O(n)**, as you must traverse the list to reach the second-last node.

**Note:** In a **doubly linked list**, if there is a pointer to the tail, deletion from the tail can be done in **O(1)**.

#### c) **Delete from a Specific Position**
- Remove the node at a specific index `k`.

**Steps:**
1. Traverse the list to the `k-1` node.
2. Adjust the pointers of the `k-1` node to skip the `k`-th node.

**Time Complexity:**
- **O(n)**, as you need to traverse the list to find the node before the one being deleted.

### 3. **Search**

Searching for an element involves traversing the list to find a node with a particular value.

**Steps:**
1. Start from the head and traverse the list.
2. Compare each node's value with the target.
3. Return the node if found, or return `null`/`None` if the element is not present.

**Time Complexity:**
- **O(n)**, where `n` is the number of nodes in the list. In the worst case, you might need to search through the entire list.

### 4. **Traversal**

Traversal means visiting each node in the list, typically for tasks like printing the list or calculating the length.

**Steps:**
1. Start from the head.
2. Move to the next node until you reach the end (`None`).

**Time Complexity:**
- **O(n)**, as you need to visit each node once.

### 5. **Reversing a Linked List**

Reversing a linked list means changing the direction of all pointers so that the last node becomes the head, and the head becomes the tail.

**Steps:**
1. Traverse the list and reverse the `next` pointers for each node.
2. Maintain three pointers: `prev`, `current`, and `next`.
3. At the end, set the last node as the new head.

**Time Complexity:**
- **O(n)**, as each node is visited once to reverse its pointer.

### 6. **Finding the Middle of a Linked List**

Using the **fast and slow pointers** technique, you can find the middle of a linked list without knowing its length in advance.

**Steps:**
1. Initialize two pointers: one slow (moving one step) and one fast (moving two steps).
2. When the fast pointer reaches the end, the slow pointer will be at the middle.

**Time Complexity:**
- **O(n)**, as each pointer moves through the list once.

### Summary of Linked List Operations and Time Complexity

| **Operation**                    | **Time Complexity** (Singly Linked List) | **Time Complexity** (Doubly Linked List) |
|-----------------------------------|------------------------------------------|------------------------------------------|
| Insert at Head                    | O(1)                                     | O(1)                                     |
| Insert at Tail                    | O(n)                                     | O(1) (with tail pointer)                 |
| Insert at Specific Position       | O(n)                                     | O(n)                                     |
| Delete from Head                  | O(1)                                     | O(1)                                     |
| Delete from Tail                  | O(n)                                     | O(1) (with tail pointer)                 |
| Delete from Specific Position     | O(n)                                     | O(n)                                     |
| Search for an Element             | O(n)                                     | O(n)                                     |
| Traversal                         | O(n)                                     | O(n)                                     |
| Reverse the List                  | O(n)                                     | O(n)                                     |
| Find Middle (Fast and Slow Pointers)| O(n)                                    | O(n)                                     |

### Key Points:
- **Singly linked lists** are simpler but less efficient for operations like deletion from the tail or bidirectional traversal.
- **Doubly linked lists** offer more efficient operations for certain tasks (like tail deletion and bidirectional traversal) but require more memory to store an additional pointer (`prev`).
- Many operations, especially insertion, deletion, and search, can have a time complexity of **O(n)** due to the need to traverse the list.