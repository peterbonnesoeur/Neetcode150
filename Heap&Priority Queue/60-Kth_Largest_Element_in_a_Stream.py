# Limit the size of the heap artificially, then do not use functions as nlargest for something so simple.

# If we need to have the nlargest of an heap of size k,
# then, use the nlargest method

import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapq.heapify(self.heap)
        if len(nums) > k:
            for i in range(len(nums) - k  ):
                heappop(self.heap)
        self.k = k

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)