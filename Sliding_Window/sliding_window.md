# Sliding window

The **sliding window** technique is a highly efficient algorithm used to solve problems involving arrays or strings, where you are required to examine contiguous subarrays or substrings. This technique helps reduce the complexity of brute-force solutions, often reducing time complexity from \(O(n^2)\) to \(O(n)\). The sliding window approach involves maintaining a window (a subset of elements) that moves (or "slides") across the array to meet the problem's requirements.

### Key Concepts of Sliding Window:

1. **Window Boundaries:** The window has two boundaries or pointers, usually called `left` and `right`. These pointers are used to maintain the size of the window, with the `right` pointer expanding the window, and the `left` pointer shrinking it when necessary.
  
2. **Dynamic Window Size:** The size of the window can either be fixed or dynamic depending on the problem:
   - **Fixed Window Size:** The window remains a fixed length throughout the algorithm.
   - **Variable Window Size:** The window size changes based on the problem conditions (e.g., expanding to include more elements, shrinking to remove invalid elements).

3. **Efficient Exploration:** Instead of recalculating results for every possible subarray, the sliding window reuses part of the work done on the previous subarray, making it more efficient.

### Types of Sliding Window Problems

#### 1. **Fixed Size Sliding Window:**

**Problem:**
Find the maximum sum of a subarray with a fixed size `k`.

**Solution:**
Use a sliding window of size `k`. Start with the sum of the first `k` elements, then slide the window by removing the leftmost element and adding the next right element at each step.

**Example:**

```python
def max_sum_subarray(arr, k):
    n = len(arr)
    if n < k:
        return None  # if the array size is smaller than k

    # Compute the sum of the first window
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide the window over the rest of the array
    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]  # add the new element, subtract the old one
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

**Time Complexity:**
- O(n), since each element is added and subtracted from the window sum exactly once.

---

#### 2. **Variable Size Sliding Window:**

**Problem:**
Find the smallest subarray with a sum greater than or equal to a given target `S`.

**Solution:**
In this case, the window size will vary. Start with an empty window and keep expanding the window by moving the `right` pointer to include new elements. Once the sum of the window exceeds or equals `S`, shrink the window by moving the `left` pointer to find the smallest possible subarray that meets the requirement.

**Example:**

```python
def smallest_subarray_with_sum(arr, S):
    n = len(arr)
    min_length = float('inf')
    current_sum = 0
    left = 0

    for right in range(n):
        current_sum += arr[right]  # expand the window by adding the right element

        # Shrink the window as small as possible while the sum is still >= S
        while current_sum >= S:
            min_length = min(min_length, right - left + 1)
            current_sum -= arr[left]  # shrink the window by removing the left element
            left += 1

    return min_length if min_length != float('inf') else 0
```

**Time Complexity:**
- O(n), as both `left` and `right` pointers only move forward, resulting in linear time complexity.

---

### Sliding Window Variants:

1. **Longest Substring with Unique Characters:**
   - Find the length of the longest substring without repeating characters.
   - **Approach:** Use a variable-sized sliding window, expanding the window with the `right` pointer and shrinking it whenever a repeated character is encountered using the `left` pointer.

   **Example:**

   ```python
   def length_of_longest_substring(s):
       char_set = set()
       left = 0
       max_length = 0

       for right in range(len(s)):
           while s[right] in char_set:
               char_set.remove(s[left])
               left += 1  # shrink the window
           char_set.add(s[right])
           max_length = max(max_length, right - left + 1)
       
       return max_length
   ```

2. **Sliding Window Maximum (Deque Approach):**
   - Given an array, find the maximum value in every sliding window of size `k`.
   - **Approach:** Use a deque (double-ended queue) to store indices of array elements. Maintain the window of indices such that the maximum element is always at the front of the deque. As the window slides, remove elements that are out of the window or smaller than the current element.

   **Example:**

   ```python
   from collections import deque

   def sliding_window_maximum(arr, k):
       dq = deque()
       result = []

       for i in range(len(arr)):
           # Remove elements not within the window
           if dq and dq[0] < i - k + 1:
               dq.popleft()

           # Remove elements smaller than the current element
           while dq and arr[dq[-1]] < arr[i]:
               dq.pop()

           dq.append(i)

           # Start appending to result after the first window is full
           if i >= k - 1:
               result.append(arr[dq[0]])

       return result
   ```

---

### Common Problems Solved Using Sliding Window:

1. **Maximum Sum Subarray of Size K (Fixed Window).**
2. **Smallest Subarray with a Given Sum (Variable Window).**
3. **Longest Substring Without Repeating Characters (Variable Window).**
4. **Sliding Window Maximum (Using Deque).**
5. **Minimum Window Substring (Finding the smallest window that contains all characters of another string).**
6. **Subarrays with K Distinct Elements.**

### Sliding Window Insights:

- The sliding window technique is best applied when you need to work with contiguous subarrays or substrings.
- When the problem involves optimizing a contiguous range (such as finding the maximum, minimum, or checking specific conditions), sliding window significantly reduces the complexity compared to a brute-force approach.
- The window size can be dynamically adjusted based on the problem's constraints, making it a versatile approach for many types of array/string-based problems.