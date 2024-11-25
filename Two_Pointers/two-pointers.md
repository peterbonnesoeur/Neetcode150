# Two pointers

Two pointers problems typically involve maintaining two distinct indices (pointers) to traverse a data structure, usually an array or string. These pointers allow you to efficiently solve problems related to searching, sorting, or subarray/substring analysis. Here are two common two-pointers problems and techniques to solve them:

## 1. Two Sum – Sorted Array (Pair with Target Sum)
**Problem**: Given a sorted array, find two numbers such that their sum equals a given target. The array is sorted in ascending order, and you need to return the indices of the two numbers.

**Solution using Two Pointers:**

Use two pointers, one starting at the beginning (left) and the other at the end (right) of the array.
If the sum of the numbers at these two pointers is equal to the target, you return the indices.
If the sum is less than the target, move the left pointer to the right to increase the sum.
If the sum is greater than the target, move the right pointer to the left to decrease the sum.
Continue until the pair is found or the pointers cross.
**Example:
**
```python
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return left, right
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None
```
**Time Complexity:**
O(n), since each pointer only moves once from one end to the other.
1. Container With Most Water
Problem: You are given an array of positive integers representing heights of lines drawn on a 2D plane. The width between two lines is the distance between their indices. Find the maximum amount of water a container can store, where the container is formed by two lines and the width between them.

**Solution using Two Pointers:
**
- Use two pointers, one at the leftmost line and the other at the rightmost line.
- The area formed between the two lines is determined by the shorter line height and the distance between the two pointers.
- Calculate the area and keep track of the maximum area encountered.
- Move the pointer corresponding to the shorter line inward, as moving the longer line won't increase the container size.
- Repeat until the pointers meet.
Example:

```python
def max_area(heights):
    left, right = 0, len(heights) - 1
    max_area = 0
    while left < right:
        height = min(heights[left], heights[right])
        width = right - left
        current_area = height * width
        max_area = max(max_area, current_area)
        
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return max_area
```
Time Complexity:

**O(n)**, because each pointer moves inward once until they meet.
Common Techniques in Two Pointers Problems:
Opposite Ends Traversal:

Use two pointers starting from opposite ends of the array and move them towards each other. This technique is useful when you need to maximize or minimize something (like in the Container with Most Water problem).
Sliding Window Approach:

In some cases, the two pointers are both on the same side, and one pointer moves forward to expand the window while the other moves to shrink the window, such as when you're searching for subarrays or substrings with specific properties.
Both problems illustrate how to efficiently process arrays or strings with minimal extra space, using the two-pointers technique to reduce the time complexity to linear time.