# Intervals

**Interval problems** are a common topic in software engineering interviews and coding challenges. These problems typically involve working with ranges of numbers (or intervals) and require efficiently handling operations like merging, inserting, or finding overlapping intervals. The key challenge in these problems is often to perform operations in an optimal way, especially when the number of intervals is large.

### Key Concepts in Interval Problems

1. **Intervals**: An interval is typically represented as a tuple or array of two elements, `[start, end]`, where `start` and `end` represent the bounds of the interval. These intervals can represent time periods, ranges of values, or other measurable quantities.

   Example:
   ```
   Interval: [2, 6] 
   This means the interval starts at 2 and ends at 6.
   ```

2. **Overlap**: Two intervals overlap if they share any common points. Two intervals `[a, b]` and `[c, d]` overlap if the following condition is met:
   ```
   a <= d and b >= c
   ```
   Example:
   ```
   [1, 5] and [4, 8] overlap because 4 <= 5.
   ```

3. **Non-overlapping**: Two intervals are non-overlapping if there is no point that is part of both intervals.

4. **Merging**: Merging intervals means combining overlapping intervals into one. For example:
   ```
   Input: [[1, 3], [2, 6], [8, 10], [15, 18]]
   Output: [[1, 6], [8, 10], [15, 18]]
   ```
   Here, the intervals `[1, 3]` and `[2, 6]` are overlapping and are merged into `[1, 6]`.

### Common Types of Interval Problems

1. **Merging Intervals**
2. **Inserting an Interval**
3. **Finding Gaps Between Intervals**
4. **Finding the Intersection of Intervals**
5. **Checking if a Set of Intervals is Non-overlapping**
6. **Interval Scheduling Problems**
7. **Overlapping Intervals Counting**

Let’s dive into each of these with explanations, example problems, and solutions.

---

### 1. **Merging Overlapping Intervals**

**Problem:**
Given a collection of intervals, merge all overlapping intervals.

**Example:**
```
Input: [[1, 3], [2, 6], [8, 10], [15, 18]]
Output: [[1, 6], [8, 10], [15, 18]]
```

**Solution Approach:**
- **Sort the intervals** by the start time.
- **Iterate through the sorted list** and merge intervals that overlap. Keep a pointer to the current interval and check the next one.
- If the current interval’s `end` is greater than or equal to the next interval’s `start`, merge them.
  
**Steps:**
1. Sort intervals by the start time.
2. Initialize a result list with the first interval.
3. For each interval, check if it overlaps with the last interval in the result list.
4. If it overlaps, merge them by updating the end time of the last interval.
5. If it doesn’t overlap, append the current interval to the result list.

**Code Example:**

```python
def merge_intervals(intervals):
    if not intervals:
        return []
    
    # Sort intervals by the start time
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]
    for i in range(1, len(intervals)):
        # Check if intervals overlap
        if merged[-1][1] >= intervals[i][0]:
            merged[-1][1] = max(merged[-1][1], intervals[i][1])  # Merge
        else:
            merged.append(intervals[i])  # No overlap, append the current interval

    return merged
```

**Time Complexity**:
- **Sorting** the intervals takes O(n log n), where `n` is the number of intervals.
- The merging process takes O(n).
- So, the overall time complexity is **O(n log n)**.

---

### 2. **Inserting an Interval**

**Problem:**
Given a set of non-overlapping intervals, insert a new interval into the list of intervals and merge if necessary.

**Example:**
```
Input: intervals = [[1, 3], [6, 9]], newInterval = [2, 5]
Output: [[1, 5], [6, 9]]
```

**Solution Approach:**
- Iterate through the existing intervals:
  - **Before the new interval**: Append intervals whose end time is before the start of the new interval.
  - **Overlap with the new interval**: Merge overlapping intervals by expanding the new interval’s bounds.
  - **After the new interval**: Append intervals whose start time is after the new interval’s end.

**Code Example:**

```python
def insert_interval(intervals, newInterval):
    result = []
    i = 0
    n = len(intervals)
    
    # Step 1: Add all intervals that end before the new interval starts
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # Step 2: Merge all overlapping intervals
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    result.append(newInterval)

    # Step 3: Add the remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1

    return result
```

**Time Complexity**:
- **O(n)** where `n` is the number of intervals, since we are doing a single pass through the list.

---

### 3. **Finding Gaps Between Intervals**

**Problem:**
Given a list of intervals, find all gaps (ranges of values) that are not covered by any intervals.

**Example:**
```
Input: [[1, 3], [5, 7], [8, 10]]
Output: [[3, 5], [7, 8]]
```

**Solution Approach:**
- First, **sort the intervals** by the start time.
- Iterate through the intervals and check if there’s a gap between the end of one interval and the start of the next.

**Code Example:**

```python
def find_gaps(intervals):
    intervals.sort(key=lambda x: x[0])
    gaps = []
    
    for i in range(1, len(intervals)):
        # If there is a gap between intervals[i-1] and intervals[i]
        if intervals[i][0] > intervals[i-1][1]:
            gaps.append([intervals[i-1][1], intervals[i][0]])
    
    return gaps
```

**Time Complexity**: 
- O(n log n) for sorting, and O(n) for finding the gaps, so the overall time complexity is **O(n log n)**.

---

### 4. **Finding the Intersection of Two Interval Lists**

**Problem:**
Given two lists of intervals, find the intersection of these two lists. An intersection of two intervals is a non-empty interval that is covered by both intervals.

**Example:**
```
Input: A = [[0, 2], [5, 10], [13, 23], [24, 25]]
       B = [[1, 5], [8, 12], [15, 24], [25, 26]]
Output: [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
```

**Solution Approach:**
- Use a **two-pointer technique**. Start at the beginning of both lists, and compare intervals:
  - If the intervals overlap, calculate the intersection and add it to the result.
  - Move the pointer that points to the interval that finishes first.

**Code Example:**

```python
def interval_intersection(A, B):
    i, j = 0, 0
    result = []
    
    while i < len(A) and j < len(B):
        # Find the overlap between A[i] and B[j]
        start = max(A[i][0], B[j][0])
        end = min(A[i][1], B[j][1])
        
        if start <= end:
            result.append([start, end])
        
        # Move the pointer of the interval that ends first
        if A[i][1] < B[j][1]:
            i += 1
        else:
            j += 1
    
    return result
```

**Time Complexity**: 
- O(n + m), where `n` and `m` are the lengths of the two interval lists.

---

### 5. **Checking if a Set of Intervals is Non-overlapping**

**Problem:**
Given a list of intervals, check if the intervals are non-overlapping.

**Solution Approach:**
- **Sort the intervals** by their start time.
- Iterate through the sorted list and check if any interval overlaps with the next one.

**Code Example:**

```python
def is_non_overlapping(intervals):
    intervals.sort(key=lambda x: x[0])
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False 