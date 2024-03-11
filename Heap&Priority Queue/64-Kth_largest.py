import heapq
# Suboptimal Nlog(N) solution:

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Convert the first k elements of the array into a min-heap.
        return heapq.nlargest(k,nums)[-1]

# The issue here is that we are processing way too many elements while iterating over the heap.

# A better solution is to use a min_heap and then iterating of the resulting few elements


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Convert the first k elements of the array into a min-heap.
        min_heap = nums[:k]
        heapq.heapify(min_heap)

        # Go through the rest of the numbers in the array.
        for num in nums[k:]:
            # If the current number is larger than the smallest number in the heap,
            # pop the smallest number from the heap and add the current number.
            if num > min_heap[0]:
                # This function is more efficient than heappop then heappush according to the doc
                heapq.heappushpop(min_heap, num)

        # The root of the heap (the first element) is the kth largest element.
        return min_heap[0]

#In this version, a min-heap is created from the first k elements of the list. Then, for each of the remaining elements in the list,
#if the element is greater than the smallest element in the heap (which is at the root of the heap), the smallest element is removed,
#and the new element is added. This ensures that the heap always contains the k largest elements of the array. Since the heap is always of size k,
#the time complexity of inserting an element is O(log k). Therefore, the overall time complexity is O(N log k)
# which is the same as before but with a significantly smaller constant factor since we're only maintaining a heap of size k rather than manipulating all N elements for each of the top k comparisons.






