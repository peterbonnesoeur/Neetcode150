# Binary Search: A Powerful Algorithm

Binary search is an efficient algorithm for solving problems involving searching for elements in a sorted array or making decisions over a range of values. It reduces the time complexity to **O(log n)** by repeatedly halving the search space.

## Common Binary Search Problems and Techniques

### 1. Finding an Element in a Sorted Array
**Problem**:  
Given a sorted array and a target value, determine if the target exists in the array. If it does, return its index; otherwise, return `-1`.

**Solution**:
1. Set two pointers: `low` at the beginning and `high` at the end of the array.
2. Find the middle index: `mid = low + (high - low) // 2`.
3. Compare the value at `arr[mid]` with the target:
   - If it matches, return `mid`.
   - If the target is smaller, search the left half (`high = mid - 1`).
   - If the target is larger, search the right half (`low = mid + 1`).
4. Repeat until `low > high`, meaning the element is not found.

**Example**:
```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

**Time Complexity**:  
**O(log n)**, as the search space is halved at each step.

---

### 2. Find the First Occurrence of a Target in a Sorted Array
**Problem**:  
Find the index of the first occurrence of a target value in a sorted array. If the target does not exist, return `-1`.

**Solution**:
1. Perform a binary search to find the target.
2. When a match is found:
   - Store the index (`result = mid`).
   - Continue searching the left half (`high = mid - 1`).
3. Return the stored index after the search is complete.

**Example**:
```python
def find_first_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == target:
            result = mid  # store the index
            high = mid - 1  # search the left half
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result
```

**Time Complexity**:  
**O(log n)**, as the search space is halved in each iteration.

---

### Common Techniques in Binary Search Problems

#### Binary Search on Answer
Binary search can find a decision boundary instead of an exact value. Examples include:
- Finding the smallest or largest possible solution that satisfies a condition.

**Example Problem**:  
Given an array of `0`s and `1`s where the transition happens from `0` to `1`, find the first index of `1`.

**Solution**:
```python
def find_first_one(arr):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == 1:
            high = mid - 1  # look for earlier 1
        else:
            low = mid + 1  # look for first 1 in the right half
    return low if low < len(arr) and arr[low] == 1 else -1
```

---

### 3. Finding the Square Root of a Number (Without Built-in Functions)
**Problem**:  
Compute the integer square root of a non-negative integer `x`.

**Solution**:
1. Define the range `[0, x]`.
2. Use binary search:
   - Compute `mid * mid` for each `mid`.
   - If `mid * mid == x`, return `mid`.
   - If `mid * mid < x`, move `low` to `mid + 1`.
   - If `mid * mid > x`, move `high` to `mid - 1`.
3. Return `high` for the integer part of the square root.

**Example**:
```python
def square_root(x):
    if x < 2:
        return x
    low, high = 1, x // 2
    while low <= high:
        mid = low + (high - low) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            low = mid + 1
        else:
            high = mid - 1
    return high  # The integer part of the square root
```

**Time Complexity**:  
**O(log x)**, as the range is halved at each step.

---

### Common Variations of Binary Search
- **Lower/Upper Bound Search**: Find the first or last occurrence of an element or the boundary where a condition holds.
- **Binary Search on Monotonic Functions**: Apply binary search to minimize or maximize solutions in problems with a monotonic behavior.

Binary search is particularly useful in problems involving sorted structures or narrowing down a decision boundary in large search spaces.